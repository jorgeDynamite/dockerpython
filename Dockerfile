FROM python:3.9

ADD main.py .

RUN pip3 install scikit-learn

CMD ["python", "./main.py"]