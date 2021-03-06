import MeCab
tagger = MeCab.Tagger('-Owakati')
with open('comment.txt', 'r') as f:
    text = f.readlines()
    for row in text:
        with open('comment_wakati.txt', 'a') as seq:
            seq.write(tagger.parse(row))
            