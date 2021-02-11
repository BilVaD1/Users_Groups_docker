FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /TZ
WORKDIR /TZ
COPY requirements.txt /TZ/

RUN pip install -r requirements.txt
ADD . /TZ/