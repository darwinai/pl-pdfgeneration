
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0] + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'pdfgeneration',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '0.1',
      description      =   'An app that takes in prediction results and generates PDF',
      long_description =   readme(),
      author           =   'DarwinAI',
      author_email     =   'jefferpeng@darwinai.ca',
      url              =   'http://wiki',
      packages         =   ['pdfgeneration'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['pdfgeneration/pdfgeneration.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
