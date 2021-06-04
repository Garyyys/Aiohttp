FROM python:3
COPY ./requirements.txt /etc/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /etc/requirements.txt

COPY . /app
WORKDIR /app

CMD python3 server.py