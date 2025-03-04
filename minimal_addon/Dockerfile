FROM python:3.9-alpine

WORKDIR /app

COPY run.sh /app/
COPY replicator.py /app/

RUN chmod +x /app/run.sh

CMD [ "/app/run.sh" ] 