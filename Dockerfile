FROM python:3.9

ADD python.py .

CMD ["python", "./python.py"]