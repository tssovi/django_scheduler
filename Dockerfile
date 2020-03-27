FROM python:2.7

COPY requirements.txt /opt/pip/requirements.txt
RUN pip install -r /opt/pip/requirements.txt

ADD . /app/
WORKDIR /app/

ENTRYPOINT celery -A django_celery worker -B --loglevel=DEBUG