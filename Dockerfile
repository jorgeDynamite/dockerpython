FROM ubuntu:latest 

RUN apt update

WORKDIR /usr/app/src/

COPY python.py ./

CMD ["python3", "./python.py"]