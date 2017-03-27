FROM ubuntu:xenial

run apt-get update
run apt-get install -y python3.6
COPY . /src
WORKDIR /src


