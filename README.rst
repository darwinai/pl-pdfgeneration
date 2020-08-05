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


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing            \
      local/pl-pdfgeneration pdfgeneration.py --imagefile ex-covid.jpeg             \
      --patientId 1234567  /incoming /outgoing               \


Examples
--------


docker build -t local/pl-pdfgeneration .

docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing local/pl-pdfgeneration pdfgeneration.py --imagefile ex-covid.jpeg --patientId 1234567  /incoming /outgoing

docker run --rm local/pl-pdfgeneration pdfgeneration.py --json