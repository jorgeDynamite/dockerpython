FROM python:3.9-slim
ADD main.py .
RUN pip install tensorflow tensorflow-io
CMD ["python", "./main.py"]