FROM python:3.9.18-slim
LABEL maintainer="Arkaprabha Das"
RUN mkdir /splitApplication/
WORKDIR /splitApplication/
COPY . /splitApplication/
#RUN apt-get update && apt-get install -y ffmpeg portaudio19-dev
RUN pip install -r requirements.txt

# Installing Speaker ID package dependencies
#RUN tar -zxvf speakerid-v1-py.tar.gz && cd speakerid-v1-py && pip install . && cd .. && rm -rf speakerid-v1-py

#ENV SERVER_PORT 8022
#ENV MODEL_TO_USE SPEAKER_ID

EXPOSE 5090

CMD python3 main.py

