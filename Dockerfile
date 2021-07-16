# Docker file for pdfgeneration ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-pdfgeneration .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-pdfgeneration .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-pdfgeneration
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-pdfgeneration
#


FROM fnndsc/ubuntu-python3:18.04
MAINTAINER fnndsc "dev@babymri.org"

RUN mkdir -p /usr/src/pdfgeneration

ENV APPROOT="/usr/src/pdfgeneration"
ENV DEBIAN_FRONTEND=noninteractive
COPY ["requirements.txt", "${APPROOT}"]

RUN apt-get update \
  && apt-get install -y libsm6 libxext6 libxrender-dev wkhtmltopdf xvfb \
  && pip install --upgrade pip \
  && pip install -r requirements.txt

COPY ["pdfgeneration", "${APPROOT}"]

WORKDIR $APPROOT

CMD ["pdfgeneration.py", "--help"]

