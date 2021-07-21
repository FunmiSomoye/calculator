FROM python:3.8-slim

# Identify the maintainer of an image
LABEL maintainer="fsomoye@aol.com"

# set working directory
WORKDIR /usr/src

# add requirements
COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src