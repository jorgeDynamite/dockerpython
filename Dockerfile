FROM ubuntu:latest 

RUN apt update

WORKDIR /usr/app/src/

COPY print.py ./

CMD ["python3", "./print.py"]