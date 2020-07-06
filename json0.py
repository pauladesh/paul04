import json

data='{"v1":"Adesh","v2":"Mukesh"}'
parsed = json.loads(data)
print(parsed['v1'])
print(parsed['v2'])

data2={
"channel":"PurnaNirogi",
"cars":['Alto','Celerio','WagonR'],
"Cupboard":('Cup',69),
"isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)
