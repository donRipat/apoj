FROM python:3.9-slim
COPY ./requirements.txt /requirements.txt
COPY ./samples/ /samples/
COPY ./app/ /app/
RUN pip install -r requirements.txt 
RUN apt-get update
RUN apt-get install ffmpeg libavcodec-extra -y

CMD ["python", "app/main.py"]
