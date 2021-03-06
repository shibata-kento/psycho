FROM continuumio/anaconda3
WORKDIR /app/
ADD requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install autopep8 && \
    pip install Keras && \
    pip install tensorflow && \
    pip install -r requirements.txt
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 

ENV PATH $MECABRC:/etc/mecabrc/

EXPOSE 8888
ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
CMD ["--notebook-dir=/workdir"]