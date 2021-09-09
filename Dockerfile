FROM ubuntu:latest
MAINTAINER Sohaib "sohaibayub9@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["extra_app.py"]