FROM python:3.9-slim
WORKDIR /app
COPY * /app
RUN pip install -r requirements.txt 
RUN apt-get update
RUN apt-get install ffmpeg libavcodec-extra -y

CMD ["python", "/app/main.py"]
