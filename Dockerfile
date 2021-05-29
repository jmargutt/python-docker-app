# base docker image
FROM python:3.7.10-buster

# install pip
RUN apt-get update && \
	apt-get install -y python3-pip && \
	ln -sfn /usr/bin/python3.7 /usr/bin/python && \
	ln -sfn /usr/bin/pip3 /usr/bin/pip

# install myapp
WORKDIR /myapp
ADD myapp .
RUN pip install .
