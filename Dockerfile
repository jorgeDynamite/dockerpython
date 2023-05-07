FROM python:3.9
ADD main.py .
RUN pip install scipy pillow requests
RUN pip install tensorflow==2.50 --no-cache-dir
RUN pip install --upgrade tensorflow-hub --no-cache-dir
CMD ["python", "./main.py"]