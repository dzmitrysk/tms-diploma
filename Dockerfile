FROM ubuntu:latest

WORKDIR /
COPY . .
RUN apt-get update && apt-get install -y python3.9 && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt &&\
    pip3 install psycopg2-binary

RUN python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py shell < create_admin.py &&\
    python3 manage.py shell < create_sample_data.py


EXPOSE 9200 5432
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:9200"]