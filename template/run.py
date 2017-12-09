#! /usr/bin/env python
import os, json, pprint

DIR = os.path.dirname(os.path.abspath(__file__))
UDIR = os.path.dirname(DIR)
TARGET = UDIR + "/ctcamp/"


htmltags = ["{{CTC_CTCAMPNUM}}", "{{CTC_TITLE}}", "{{CTC_MANAGER}}", "{{CTC_DESCRIPTION}}"]
jsontags = ["CT Camp 기수", "ID", "담당자", "제목", "부제", "설명"]
jsondata = []

template = open("template.html", "r")

for line in open(UDIR + "/xls2json/contents.json") :
	jsondata.append(json.loads(line))

pprint.pprint(jsondata)

origin_string = template.read()

def MakeIndex(jsondata) :
	



	

def MakeContents(jsondata) :
	for data in jsondata[1:] :
		TARGET_DIR = TARGET + "ctcamp" + data["CT Camp 기수"] + "/contents/"
		
		if not os.path.exists(TARGET_DIR):
			os.makedirs(TARGET_DIR)

		target_string = origin_string;

		outfile = open(TARGET_DIR + data["ID"] + ".html", "w")
		
		#print(target_string)

		target_string = target_string.replace("{{CTC_CTCAMPNUM}}", "CT CAMP " + data["CT Camp 기수"])
		target_string = target_string.replace("{{CTC_TITLE}}", data["제목"])
		target_string = target_string.replace("{{CTC_MANAGER}}", data["담당자"])
		target_string = target_string.replace("{{CTC_DESCRIPTION}}", data["설명"])


		print(target_string)
		
		outfile.write(target_string)
		outfile.close()



MakeIndex(jsondata)
MakeContents(jsondata)









