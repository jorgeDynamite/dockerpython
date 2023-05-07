FROM ubuntu:latest 

RUN apt update

RUN sudo apt install python3 -y

WORKDIR /usr/app/src/

COPY python.py ./

CMD ["python3", "./python.py"]