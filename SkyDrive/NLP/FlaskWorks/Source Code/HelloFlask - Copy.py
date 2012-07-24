'# -*- coding: utf-8 -*-'
from __future__ import division

''' This module alalyses Shakespeare's Documents The module should be called after
actibvating the module GatherFiles.PY '''

__author__ = 'Dr Avner OTTENSOOSER <avner.ottensooser@gmail.com>'
__version__ = '$Revision: 0.01 $'


AO_ROOT_PATH         =  'C:\\Users\\Avner\\SkyDrive\\NLP\\'
AO_PROJECT_NAME      =  'FlaskNLPworks'
AO_sCommonPath       =  AO_ROOT_PATH + 'CommonWorks\\'
AO_sCommonCode       =  AO_sCommonPath + 'Source Code'
AO_sCompelationSite  =  AO_ROOT_PATH + AO_PROJECT_NAME + '\\'
AO_sModulesPath      =  AO_sCompelationSite + 'Source Code'

from werkzeug.wrappers import Request, Response
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
# configuration
DEBUG = True
SECRET_KEY = ’development key’
USERNAME = ’admin’
PASSWORD = ’default’
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

import sys
sys.path.append(AO_sCommonCode)
import AO_mOpinionWords

@Request.application
def AO_lApplication(request):
    AO_sDocument= 'Not a single very charming fat cat sat on the mat.'
    AO_lOpinion = AO_mOpinionWords.AO_lAssessOpinion(AO_sDocument)
    return Response(AO_lOpinion)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, AO_lApplication)