FROM python:3.9
ADD main.py .
RUN pip install tensorflow==2.5.0 --no-cache-dir
CMD ["python", "./main.py"]