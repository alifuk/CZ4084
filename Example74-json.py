import json
'''
with open("studenti.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["albert"])
'''
lidi = {
    "nunu": 90,
    "stul": 300,
    "kytka": 200
}

with open("studenti.json", "w", encoding="utf-8") as f:
    json.dump(lidi,f)

v_retezci = json.dumps(lidi)
print(v_retezci)
print(type(v_retezci))
lidi2 = json.loads(v_retezci)
print(lidi2)
print(type(lidi2))

