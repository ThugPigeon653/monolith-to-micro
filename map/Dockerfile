FROM python:3.9

WORKDIR /app

COPY map.py /app/ 
COPY config/ /app/config

RUN pip install pyqt5

CMD ["python", "/app/map.py"]