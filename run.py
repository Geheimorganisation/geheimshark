#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from selfshark import app

# FLASK CONFIGURATION; PLEASE CHANGE FOR PRODUCTIVE USE; LOOK AT http://flask.pocoo.org/docs/config/#builtin-configuration-values
DEBUG = True
SECRET_KEY = "SbfCyv39HM6oOci516J2RZurvLD6uhHfDiOkNZpUZo"

app.config.from_object(__name__)

# run the app
app.run()
