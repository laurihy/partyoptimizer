#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

try:
  source = sys.argv[1]
  target = sys.argv[2]
except:
  raise SystemExit, 'Didnt get source and target, terminating'

try:
  sourcefile = open(source,'r').read()
  targetfile = open(target,'w')
except:
  raise SystemExit, 'Couldnt open source and target, terminating'

def generateCell(data):
  ret = '<td>'
  ret+='<h1>Id: '+str(data['id'])+'</h1>'
  ret+='<p>Gender: '+str(data['gender'])+'</p>'
  ret+='<p>Avec: '+str(data['avec'])+'</p>'
  ret+='<p>Friends: '+str(data['friends'])+'</p>'
  ret+='<p>Score: '+str(data['fitness'])+'</p>'
  ret+='</td>'

  return ret

def generateTable(data):
  ret = '<table>'
  i = 0
  for d in data:
    if i%2 == 0: ret+='<tr>'
    ret+=generateCell(d)
    if i%2 == 1: ret+='</tr>'
    i+=1
  ret+='</table>'
  return ret

def generateHtml(data):
  table = generateTable(data)

  style = '<link href="style.css" rel="stylesheet" type="text/css">'

  return "<html><head>"+style+"<title>ASD</title></head><body>"+table+"</body></html>"

sourcejson = json.loads(sourcefile)

# our data stores score for participants individually, attach it to it

for i in range(len(sourcejson[1])):
  sourcejson[1][i]['fitness'] = sourcejson[2][i] 

html = generateHtml(sourcejson[1])
targetfile.write(html);
print 'DONE'



