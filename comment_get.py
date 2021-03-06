import requests
import json
import csv
import pandas as pd

URL = 'https://www.googleapis.com/youtube/v3/'
with open('token.txt', 'r') as f:
    API_KEY = f.read()
VIDEO_ID = 'VCQ6ft5jSew'
def print_video_comment(no, video_id, next_page_token):
    params = {
        'key': API_KEY,
        'part': 'snippet',
        'videoId': video_id,
        'order': 'relevance',
        'textFormat': 'plaintext',
        'maxResults': 100,
    }
    tmp = [[]]
    if next_page_token is not None:
        params['pageToken'] = next_page_token
    response = requests.get(URL + 'commentThreads', params=params)
    resource = response.json()

    for comment_info in resource['items']:
        text = comment_info['snippet']['topLevelComment']['snippet']['textDisplay']
        if text[-2:] == 'そう':
            tmp[0] = text.replace('\n', '')
            writer.writerow(tmp)
            # print(text)
        parentId = comment_info['snippet']['topLevelComment']['id']
        no = no + 1

    if 'nextPageToken' in resource:
        print_video_comment(no, video_id, resource["nextPageToken"])

video_id = VIDEO_ID
no = 1
with open('comment.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['comment'])
    print_video_comment(no, video_id, None)
