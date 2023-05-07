FROM python:3.9
ADD main.py .
RUN apt-get update && apt-get install -y python3-pip
RUN pip install pillow
CMD ["python", "./main.py"]