import csv
import json

csvfile = open('contents.csv', 'r')
jsonfile = open('contents.json', 'w')

fieldnames = ("CT Camp 기수","ID","제목","부제","담당자","설명")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
  json.dump(row, jsonfile)
  jsonfile.write('\n')

