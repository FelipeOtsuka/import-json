import json

i = open('jooj.json', )
data = json.load(i)
for f in data["lote_informções"]:
    print(f)
