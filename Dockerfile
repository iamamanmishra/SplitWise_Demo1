FROM python:3.9.18-slim
LABEL maintainer="Arkaprabha Das"
RUN mkdir /splitApplication/
WORKDIR /splitApplication/
COPY . /splitApplication/
RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 5090

CMD python3 main.py

