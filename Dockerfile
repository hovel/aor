FROM danielwhatmuff/zappa:latest
MAINTAINER Pavel Zhukov (gelios@gmail.com)

ADD . /root/src/
RUN mkdir /root/logs/

RUN rpm --rebuilddb && yum install -y python-devel zlib-devel libjpeg-turbo-devel

RUN pip install --upgrade "pip==9.0.1" wheel "setuptools<39.0"
RUN pip install ansible

RUN virtualenv /var/venv

RUN source /var/venv/bin/activate && pip install --upgrade "pip==9.0.1" wheel "setuptools<39.0"
RUN source /var/venv/bin/activate && pip install -r /root/src/requirements.txt -U

EXPOSE 80