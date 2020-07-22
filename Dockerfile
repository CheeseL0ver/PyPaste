FROM python:3

ENV PASTEBIN_DEV_KEY YOUR_API_KEY 
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src/
WORKDIR /src
CMD ["bash"]
