# FROM имя_базового_образа:тег
FROM python:3.12.5-alpine

WORKDIR /usr/workspace

# COPY ./file /container_directory
COPY ./ /usr/workspace

RUN pip3 install -r requirements.txt

CMD ['python3', '/usr/workspace/tests']
