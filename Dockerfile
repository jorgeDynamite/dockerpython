FROM python:3.10
ADD main.py .
RUN pip install scipy pillow requests
RUN pip install tensorflow --no-cache-dir
CMD ["python", "./main.py"]