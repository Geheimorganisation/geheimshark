# -*- coding: utf-8 -*-
from selfshark import app, conf
from flask import render_template, request
from mutagen.easyid3 import EasyID3
import json, os, hashlib

@app.route("/api/get/search")
def search():
	taglist = getSongs()

	# search for songs
	songlist = []
	for s in taglist:
		if request.args["q"].lower() in s["q"]:
			songlist.append(s)

	return json.dumps(songlist)

@app.route("/api/get/id")
def id():
	songs = getSongs()

	for s in songs:
		if s["id"] == request.args["id"]:
			return json.dumps(s)

## helper functions ##
# from https://mayankjohri.wordpress.com/2008/07/02/create-list-of-files-in-a-dir-tree/
def recursivListDir(dir):
	fileList = []
	for root, subFolders, files in os.walk(dir):
		for file in files:
			fileList.append(os.path.join(root,file))

	return fileList

def getSongs():
	# get all files
	files = recursivListDir(conf["musicDir"])

	# get all id3 tags
	taglist = []
	for f in files:
		tags = EasyID3(f)
		taglist.append({
			"file":		f.replace(conf["mDirRepl"], ""),
			"id":		hashlib.sha1(f.replace(conf["mDirRepl"], "")).hexdigest(),
			"title":	tags["title"],
			"artist":	tags["artist"],
			"q":		"{0} {1}".format(
							tags["title"][0],
							tags["artist"][0]
						).lower()
		})

	return taglist