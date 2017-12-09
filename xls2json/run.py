#!/usr/bin/env python
import csv
import json

csvfile = open('contents.csv', 'r')
jsonfile = open('contents.json', 'w')

fieldnames = ("ctcampnum","id","tilte","subtitle","manager","description")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
  json.dump(row, jsonfile)
  jsonfile.write('\n')

