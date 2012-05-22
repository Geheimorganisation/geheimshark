# -*- coding: utf-8 -*-
import sys
from flask import Flask

## CONFIGURATION ##
conf = {
	"musicDir":	"selfshark/static/music/",
	"mDirRepl":	"selfshark/"
}

## APP ##

# set utf-8 as default
reload(sys)
sys.setdefaultencoding("utf-8")

# the app
app = Flask(__name__)

# VIEWS AND FILTERS
import selfshark.start
import selfshark.api