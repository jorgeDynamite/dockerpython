FROM python:3.9
ADD main.py .
RUN pip install --index-url=https://pypi.python.org/simple/requests/
CMD ["python", "./main.py"]