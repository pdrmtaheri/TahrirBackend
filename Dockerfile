FROM python:3.7

RUN apt-get update --fix-missing && apt-get install -qqy postgresql-client

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

EXPOSE 55555
ENTRYPOINT ["./docker-entrypoint.sh"]
