FROM python:latest

WORKDIR /opt/ApplovinSDK

ADD https://bootstrap.pypa.io/get-pip.py /root/get-pip.py

RUN python /root/get-pip.py
RUN pip install pipenv
RUN pipenv install requests
RUN pip install mypy

COPY . /opt/ApplovinSDK

VOLUME /opt/ApplovinSDK
