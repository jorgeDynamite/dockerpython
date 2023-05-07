FROM python:3.9-slim
ADD main.py .
RUN pip install pillow
CMD ["python", "./main.py"]