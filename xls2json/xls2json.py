#! /usr/bin/env python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import json

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('ctcamp_content.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_key("1KwEmtiQTwN0BMShbC7AXZFmJUs_KhJ1o_4MfUl6Fp-g").sheet1


export_file = wks.export(format='csv')
f = open('contents.csv', 'wb')
f.write(export_file)
f.close()


csvfile = open('contents.csv', 'r')
jsonfile = open('contents.json', 'w')

fieldnames = ("conference","id","title","subtitle","manager","description", "ppt")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
	if row['id'] == 'id' :
		continue;
	json.dump(row, jsonfile, ensure_ascii = False)
	jsonfile.write('\n')

