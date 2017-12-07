FROM danielwhatmuff/zappa:latest
MAINTAINER Pavel Zhukov (gelios@gmail.com)

ADD . /root/src/
RUN mkdir /root/logs/

RUN rpm --rebuilddb && yum install -y python-devel zlib-devel libjpeg-turbo-devel

RUN pip install --upgrade pip wheel
RUN pip install ansible boto boto3

RUN source /var/venv/bin/activate && pip install --upgrade pip wheel
RUN source /var/venv/bin/activate && pip install -r /root/src/requirements.txt -U
