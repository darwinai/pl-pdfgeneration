pl-pdfgeneration
================================

.. image:: https://img.shields.io/github/license/FNNDSC/pl-pdfgeneration
    :target: https://github.com/FNNDSC/pl-pdfgeneration/blob/master/LICENSE
    :alt: License AGPL-3.0

.. image:: https://img.shields.io/docker/v/fnndsc/pl-covidnet-pdfgeneration?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-covidnet-pdfgeneration
    :alt: Version

.. contents:: Table of Contents


Abstract
--------

Generate a simple PDF report for the results from
`pl-covidnet <https://github.com/FNNDSC/pl-covidnet>`_.

Comments
--------

* Not working on PowerPC.
* Something like this should use jinja2 and LaTeX instead.

Agruments
---------

.. code::

    [--imagefile]
    required field, the name of the patient chest X-Ray image

    [--patientId]
    name to appear in report


Examples
--------

.. code::

    mkdir covidnet-in covidnet-out pdfgeneration-out
    cp chest-scan.jpg covidnet-in

    docker run --rm -u -u $(id -u):$(id -g) \
        -v $PWD/covidnet-in:/incoming:ro -v $PWD/covidnet-out:/outgoing:rw \
        fnndsc/pl-covidnet:0.2.0 covidnet \
        --imagefile chest-scan.jpg /incoming /outgoing

    docker run --rm -u -u $(id -u):$(id -g) \
        -v $PWD/covidnet-out:/incoming:ro -v $PWD/pdfgeneration-out:/outgoing:rw \
        fnndsc/pl-covidnet-pdfgeneration:0.2.0 pdfgeneration \
        --imagefile chest-scan.jpg --patientId 12345678 /incoming /outgoing
