FROM python:3.9
ADD main.py .
ADD model.pkl .
RUN pip install scipy pillow requests 
RUN pip install tensorflow==2.5.0 --no-cache-dir
RUN pip install pickle4
CMD ["python", "./main.py"]