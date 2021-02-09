FROM python:3.9.1-alpine

WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install .

CMD ["pdfgeneration", "--help"]
