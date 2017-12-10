#! /usr/bin/env python
import os, json, pprint

DIR = os.path.dirname(os.path.abspath(__file__))
UDIR = os.path.dirname(DIR)
TARGET = UDIR + "/ctcamp/"


htmltags = ["{{CTC_CONFERENCE}}", "{{CTC_TITLE}}", "{{CTC_MANAGER}}", "{{CTC_DESCRIPTION}}"]
jsontags = ["conference", "id", "manager", "title", "subtitle", "description", "ppt"]
jsondata = []

template = open("template.html", "r")

for line in open(UDIR + "/xls2json/contents.json") :
	jsondata.append(json.loads(line))

pprint.pprint(jsondata)

origin_string = template.read()


def MakeContents(jsondata) :
	for data in jsondata[1:] :
		TARGET_DIR = TARGET + data["conference"] + "/contents/"
		
		if not os.path.exists(TARGET_DIR):
			os.makedirs(TARGET_DIR)

		target_string = origin_string;

		outfile = open(TARGET_DIR + data["id"] + ".html", "w")
		
		#print(target_string)

		target_string = target_string.replace("{{CTC_CONFERENCE}}","/" + data["conference"].upper())
		target_string = target_string.replace("{{CTC_TITLE}}", data["title"])
		target_string = target_string.replace("{{CTC_SUBTITLE}}", data["subtitle"])
		target_string = target_string.replace("{{CTC_MANAGER}}", data["manager"])
		target_string = target_string.replace("{{CTC_DESCRIPTION}}", data["description"])
		target_string = target_string.replace("{{CTC_PPT_PATH}}", "/static/slides/" + data["ppt"] + ".swf")


		print(target_string)
		
		outfile.write(target_string)
		outfile.close()



MakeContents(jsondata)









