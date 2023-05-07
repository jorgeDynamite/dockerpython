FROM python:3.9
ADD main.py .
RUN pip install scipy pillow requests
RUN pip install tensorflow --no-cache-dir
RUN pip install --upgrade tensorflow-hub
CMD ["python", "./main.py"]