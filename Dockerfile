FROM python:3.9.1-slim-buster

LABEL org.opencontainers.image.authors="DarwinAI <support@darwinai.com>"

ENV DEBIAN_FRONTEND=noninteractive

COPY ["apt-requirements.txt", "requirements.txt", "./"]

RUN apt-get update \
  && xargs -d '\n' -a apt-requirements.txt apt-get install -y \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && rm -f requirements.txt apt-requirements.txt

WORKDIR /usr/local/src
COPY . .
RUN pip install .

CMD ["pdfgeneration", "--help"]
