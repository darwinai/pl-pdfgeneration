pl-pdfgeneration
================================

.. image:: https://badge.fury.io/py/pdfgeneration.svg
    :target: https://badge.fury.io/py/pdfgeneration

.. image:: https://travis-ci.org/FNNDSC/pdfgeneration.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/pdfgeneration

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-pdfgeneration

.. contents:: Table of Contents


Abstract
--------

An app that takes in prediction results and generates PDF


Synopsis
--------

.. code::

    python pdfgeneration.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 

Description
-----------

``pdfgeneration.py`` is a ChRIS-based application that...

Agruments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.

    [--imagefile]
    required field, the name of the patient chest X-Ray image

    [--patientId]
    patient's id


Local Build
-----------

.. code:: bash

    DOCKER_BUILDKIT=1 docker build -t local/pl-covidnet-pdfgeneration .

Run
----

.. code:: bash

    docker run --rm -u $(id -u):$(id -g) \
        -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw \
        darwinai/pl-covidnet covidnet \
        --imagefile ex-covid.jpg /incoming /outgoing

    docker run --rm -u $(id -u):$(id -g) \
        -v $PWD/out:/incoming:ro -v $PWD/out:/outgoing:rw \
        darwinai/pl-covidnet-pdfgeneration pdfgeneration \
        --imagefile ex-covid.jpg --patientId 12345678 /incoming /outgoing
