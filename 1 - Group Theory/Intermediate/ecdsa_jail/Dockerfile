# start by pulling the python image
FROM python:3.10-alpine

RUN apk update && apk add python3-dev gcc musl-dev gmp-dev socat
RUN pip install fastecdsa

COPY ./chal.py /srv/app/run.py
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 555 /srv/app/run.py

WORKDIR /srv/app

CMD [ "socat", "TCP-LISTEN:8000,nodelay,reuseaddr,fork", "EXEC:\"timeout -s KILL 10m python3.10 -u /srv/app/run.py\"" ]
# docker build -t ecdsa_jail <folder_path_containing_challenge_files>