FROM ubuntu:latest 

RUN yum update
RUN yum install python3 -y 

WORKDIR /usr/app/src/

COPY print.py ./

CMD ["python3", "./print.py"]