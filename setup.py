from os import path

from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name='pdfgeneration',
    # for best practices make this version the same as the VERSION class variable
    # defined in your ChrisApp-derived Python class
    version='1.1.0',
    description='An app that takes in prediction results and generates PDF',
    long_description=readme,
    author='DarwinAI',
    author_email='jefferpeng@darwinai.ca',
    url='https://github.com/darwinai/pl-pdfgeneration',
    packages=['pdfgeneration'],
    install_requires=['chrisapp', 'pudb'],
    test_suite='nose.collector',
    tests_require=['nose'],
    license='AGPL',
    python_requires='>=3.6',
    package_data={'pdfgeneration': ['template/*', 'template/assets/*']},
    entry_points={
        'console_scripts': ['pdfgeneration = pdfgeneration.__main__:main']
    },
    zip_safe=False)
