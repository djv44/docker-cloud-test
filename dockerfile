FROM ubuntu:xenial
RUN apt-get update
RUN apt-get -y install python3.6
COPY . /src
WORKDIR /src


