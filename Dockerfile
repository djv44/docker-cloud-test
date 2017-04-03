FROM ubuntu:xenial
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install flask
COPY . /src
WORKDIR /src


