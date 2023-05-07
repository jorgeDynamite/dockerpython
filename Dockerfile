FROM ubuntu:latest 

RUN apt-get update

RUN apt-get install -y python3 

WORKDIR /usr/app/src/

COPY python.py ./

CMD ["python3", "./python.py"]