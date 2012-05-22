# -*- coding: utf-8 -*-
from selfshark import app
from flask import render_template

@app.route("/")
def index():
	title = "selfshark"
	return render_template("start.html", title=title)