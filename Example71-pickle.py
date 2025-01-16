from attr import dataclass

petr = "Petr"   #do souboru jmeno.txt
with open("jmeno.txt", "w", encoding="utf-8") as f:
    f.write(petr)

with open("jmeno.txt", "r", encoding="utf-8") as f:
    print("V souboru jsou tyto řádky:")
    print(f.readlines())

@dataclass
class Tovarna:
    pocet_zamestnancu : int
    jmeno_sefa : str
continental = Tovarna(40000, "Petr")

import pickle
with open("tovarna.pickle", "wb") as f:
    pickle.dump(continental, f)

with open("tovarna.pickle", "rb") as f:
    nacteny_conti = pickle.load(f)
print(nacteny_conti)

