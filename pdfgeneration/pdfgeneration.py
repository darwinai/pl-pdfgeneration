#!/usr/bin/env python                                            
#
# pdfgeneration ds ChRIS plugin app
#
# (c) 2019-2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
from os import path
import json
import shutil
import pdfkit
import datetime
from importlib.resources import files
from chrisapp.base import ChrisApp


Gstr_title = """
 _____ _____  _   _ ___________        _   _      _    __________________   _____                           _   _             
/  __ \  _  || | | |_   _|  _  \      | \ | |    | |   | ___ \  _  \  ___| |  __ \                         | | (_)            
| /  \/ | | || | | | | | | | | |______|  \| | ___| |_  | |_/ / | | | |_    | |  \/ ___ _ __   ___ _ __ __ _| |_ _  ___  _ __  
| |   | | | || | | | | | | | | |______| . ` |/ _ \ __| |  __/| | | |  _|   | | __ / _ \ '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \ 
| \__/\ \_/ /\ \_/ /_| |_| |/ /       | |\  |  __/ |_  | |   | |/ /| |     | |_\ \  __/ | | |  __/ | | (_| | |_| | (_) | | | |
 \____/\___/  \___/ \___/|___/        \_| \_/\___|\__| \_|   |___/ \_|      \____/\___|_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|
"""


class Pdfgeneration(ChrisApp):
    """
    An app that takes in prediction results and generates PDF.
    """
    PACKAGE                 = __package__
    TITLE                   = 'PDF generation plugin'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--imagefile', 
            dest         = 'imagefile', 
            type         = str, 
            optional     = False,
            help         = 'Name of image file submitted to the analysis')
        self.add_argument('--patientId', 
            dest         = 'patientId', 
            type         = str, 
            optional     = True,
            default      = 'not specified',
            help         = 'Patient ID')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        # fetch input data
        with open('{}/prediction-default.json'.format(options.inputdir)) as f:
          classification_data = json.load(f)
        try: 
            with open('{}/severity.json'.format(options.inputdir)) as f:
                severityScores = json.load(f)
        except:
            severityScores = None

        template_file = "pdf-covid-positive-template.html" 
        if classification_data['prediction'] != "COVID-19" or severityScores is None:
            template_file = "pdf-covid-negative-template.html"

        txt = files('pdfgeneration').joinpath('template').joinpath(template_file).read_text()
        # replace the values
        txt = txt.replace("${PATIENT_TOKEN}", options.patientId)
        txt = txt.replace("${PREDICTION_CLASSIFICATION}", classification_data['prediction'])
        txt = txt.replace("${COVID-19}", classification_data['COVID-19'])
        txt = txt.replace("${NORMAL}", classification_data['Normal'])
        txt = txt.replace("${PNEUMONIA}", classification_data['Pneumonia'])
        txt = txt.replace("${X-RAY-IMAGE}", options.imagefile)

        time = datetime.datetime.now()
        txt = txt.replace("${month-date}", time.strftime("%c"))
        txt = txt.replace("${year}", time.strftime("%Y"))
        # add the severity value if prediction is covid
        if template_file == "pdf-covid-positive-template.html":
            txt = txt.replace("${GEO_SEVERITY}", severityScores["Geographic severity"])
            txt = txt.replace("${GEO_EXTENT_SCORE}", severityScores["Geographic extent score"])
            txt = txt.replace("${OPC_SEVERITY}", severityScores["Opacity severity"])
            txt = txt.replace("${OPC_EXTENT_SCORE}", severityScores['Opacity extent score'])

        # pdfkit wkhtmltopdf is hard-coded to look in /tmp for assets
        # when input is a string
        for asset_file in files('pdfgeneration').joinpath('template/assets').iterdir():
            os.symlink(asset_file, path.join('/tmp', asset_file.name))
        os.symlink(path.join(options.inputdir, options.imagefile), path.join('/tmp', options.imagefile))

        pdfkit.from_string(txt, path.join(options.outputdir, 'patient_analysis.pdf'))

    def show_man_page(self):
        self.print_help()
