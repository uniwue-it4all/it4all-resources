FROM mongo

RUN apt update && \
  apt install -y python3 python3-pip locales && \
  sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen && \
  pip3 install dataclasses pymongo colorama typing_extensions

# Set the locale
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

WORKDIR /app

COPY ./ /app/

COPY ./seed.sh /docker-entrypoint-initdb.d/seed.sh
