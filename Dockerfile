FROM python:3-alpine

ARG WorkDir=/app/

WORKDIR ${WorkDir}

COPY . ${WorkDir}

RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python server.py