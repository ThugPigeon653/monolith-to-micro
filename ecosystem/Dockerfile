FROM python:3.9

ENV SQL_SERVER="localhost"
ENV SQL_DATABASE="master"
ENV SQL_UID="sa"
ENV SQL_PWD="StrongPword8"

WORKDIR /app

COPY ecosystem.py /app/

RUN pip install psycopg2-binary

CMD ["python", "/app/ecosystem.py"]