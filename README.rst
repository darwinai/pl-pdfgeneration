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


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a 

.. code:: bash

    pip install pdfgeneration

and run with

.. code:: bash

    pdfgeneration.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    pdfgeneration.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                         \
        pl-pdfgeneration pdfgeneration.py                         \
        --imagefile ex-covid.jpeg /incoming /outgoing                        \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-pdfgeneration pdfgeneration.py                        \
            --man                                                       \
            /incoming /outgoing

Examples
--------



docker build -t pl-pdfgeneration .

docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing pl-pdfgeneration pdfgeneration.py --imagefile ex-covid.jpeg /incoming /outgoing

