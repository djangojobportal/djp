#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
FROM alisonmukoma/django-base:3.7
MAINTAINER Alison Mukoma <mukomalison@gmail.com>

#RUN  ln -s /bin/true /sbin/initctl

# Pandoc needed to generate rst dumps, uic compressor needed for django-pipeline
RUN apt-get update -y; apt-get -y --force-yes install yui-compressor

ADD REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip3 install -r /REQUIREMENTS.txt
RUN pip3 install uwsgi


# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 8080

#USER www-data

WORKDIR /home/web/django_project
CMD ["uwsgi", "--ini", "/uwsgi.conf"]
