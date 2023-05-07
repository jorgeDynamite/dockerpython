FROM python:3.9-slim
ADD main.py .
RUN sudo apt-get install --reinstall python3-pip
RUN pip install pillow
CMD ["python", "./main.py"]