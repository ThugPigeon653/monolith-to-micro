FROM python:3.9

WORKDIR /app

ENV SQL_SERVER="localhost"
ENV SQL_DATABASE="master"
ENV SQL_UID="sa"
ENV SQL_PWD="StrongPword8"

COPY map.py /app/ 
COPY config/ /app/config

RUN pip install requests

CMD ["python", "/app/map.py"]