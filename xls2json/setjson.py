#! /usr/bin/env python
import json

jsoncontent = open('/home/mantis/CTcamp/CTCampWeb/ctcamp/scripts/contentslist.js', 'w')

header = 'if (typeof g_sessionSrcList == "undefined") g_contentsList = [];\n'
header += 'g_contentsList.push(\n'

jsoncontent.write(header)

data=[]

for line in open("/home/mantis/CTcamp/CTCampWeb/xls2json/contents.json") :
	data.append(json.loads(line))
	print(data)

print(data)

dic = {
	'contents' : data
}

json.dump(dic, jsoncontent, ensure_ascii = False)

jsoncontent.write(');\n')
