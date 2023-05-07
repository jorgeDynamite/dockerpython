FROM python:3.9
ADD main.py .
RUN pip -m install tensorflow
CMD ["python", "./main.py"]