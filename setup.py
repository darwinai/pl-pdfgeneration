from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             =   'pdfgeneration',
    version          =   '0.2.0',
    description      =   'An app that takes in COVID-Net prediction results and generates PDF',
    long_description =   readme,
    author           =   'DarwinAI',
    author_email     =   'jefferpeng@darwinai.ca',
    url              =   'https://github.com/FNNDSC/pl-pdfgeneration',
    packages         =   ['pdfgeneration'],
    install_requires =   ['chrisapp'],
    test_suite       =   'nose.collector',
    tests_require    =   ['nose'],
    license          =   'MIT',
    zip_safe         =   False,
    python_requires  =   '>=3.8',
    package_data     = {
        'pdfgeneration': ['template/*', 'template/assets/*']
    },
    entry_points     = {
        'console_scripts': [
            'pdfgeneration = pdfgeneration.__main__:main'
            ]
        }
)
