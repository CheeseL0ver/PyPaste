FROM python:3

ENV PASTEBIN_DEV_KEY 299d106ba736f583943699f1e73f405c 
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src/
WORKDIR /src
CMD ["bash"]
