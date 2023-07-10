FROM python:3.10-alpine

#RUN apk add --update --no-cache mariadb mariadb-client

WORKDIR /data
COPY requirements.txt requirements.txt
RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev mariadb-dev && pip install --no-cache-dir -r requirements.txt && apk del build-base
COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
