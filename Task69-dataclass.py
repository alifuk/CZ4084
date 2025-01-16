
#implementujte dataclass Letadlo, Zamestnanec, Aerolinie
from dataclasses import dataclass

@dataclass
class Letadlo:
    kapacita : int
    dolet : int
    rychlost : int

@dataclass
class Zamestnanec:
    vek : int
    plat : int
    naletano : int

@dataclass
class Aerolinie:
    pocet_letadel : int
    zamestnancu : int
    incidenty : int

#Na kod níže nesahat
boeing737 = Letadlo(250, 3500,750) #250 kapacita, 3500 dolet, 750 rychlost
kapitan = Zamestnanec(40, 200000, 2000) #věk, plat, nalétáno na stroji
smartwings = Aerolinie(30, 400, 1)#počet letadel, zaměstnanců, počet incidentů

print(boeing737)
print(kapitan)
print(smartwings)

