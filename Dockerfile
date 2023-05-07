FROM python:3.9

ADD python.py .

RUN pip install scikit-learn

CMD ["python", "./python.py"]