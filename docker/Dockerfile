#Grab the latest alpine image
FROM alpine:latest

MAINTAINER Sergi Torrellas

# Add folder
RUN apk add --no-cache --update python3 bash postgresql-dev build-base python3-dev
ADD . /repo/
WORKDIR /repo/
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations api
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --no-input

EXPOSE 8000

# Run container
#CMD python3 /repo/manage.py runserver 0.0.0.0:$PORT
CMD gunicorn sustainability.wsgi --bind 0.0.0.0:$PORT
#sudo docker run -t -p8080:8080 -e"PORT=8080" sustainability
