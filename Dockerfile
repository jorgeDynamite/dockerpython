FROM python:3.9
ADD main.py .
RUN pip3 install pillow
CMD ["python", "./main.py"]