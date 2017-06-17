FROM python:3.6

MAINTAINER Natalie

ENV BUILD_NUMBER=0.0.1

WORKDIR /talk_app
EXPOSE 5000

RUN pip install --upgrade pip

COPY . /talk_app

RUN pip3 install -r /talk_app/requirements.txt

CMD ["python3", "talk_app.py"]
