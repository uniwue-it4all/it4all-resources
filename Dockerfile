FROM python:3-alpine

ARG WorkDir=/app/

COPY requirements.txt requirements.txt

RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

WORKDIR ${WorkDir}

# FIXME: move resources to different directory!
COPY . ${WorkDir}

EXPOSE 5000

ENTRYPOINT python server.py