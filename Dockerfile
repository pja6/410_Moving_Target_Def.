FROM ubuntu:23.10
COPY fServer.py ./
COPY controller.py ./
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python3
RUN apt-get install -y python3-flask

CMD ["python3", "controller.py"]
