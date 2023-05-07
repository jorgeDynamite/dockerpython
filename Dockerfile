FROM ubuntu:latest 

RUN apt update && apt upgrade

RUN apt install wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install python3.11

WORKDIR /usr/app/src/

COPY python.py ./

CMD ["python3", "./python.py"]