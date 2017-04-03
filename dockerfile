FROM ubuntu:xenial
RUN apt-get update
COPY . /src
WORKDIR /src


