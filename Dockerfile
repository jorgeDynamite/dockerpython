FROM python:3.9
ADD main.py .
RUN mkdir /model1

# copy files from host machine to the directory inside the container
COPY ./model1 /model1
RUN pip install scipy pillow requests joblib
RUN pip install tensorflow==2.5.0 --no-cache-dir
CMD ["python", "./main.py"]