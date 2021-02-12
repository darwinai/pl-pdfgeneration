FROM python:3.9.1-slim-buster

RUN apt-get update \
    && apt-get install -y wkhtmltopdf xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install .

CMD ["pdfgeneration", "--help"]
