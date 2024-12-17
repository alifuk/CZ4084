cislo = 1
while cislo < 5 : # cislo < 5    ==>   1 < 5     ==>     True
    print(f"Cislo {cislo} je < 5 ")
    cislo += 1
    pass
'''
jmena = []
while len(jmena) < 4:
    jmena.append(input("Zadej jméno"))
    print(jmena)
'''
import random
a = random.randint(0,100)
print(a)


def pozdrav(jmeno):
    if jmeno[0] == "A":
        print(f"Tvoje název je na začátku abecedy, můžeš předběhnout frontu. Díky {jmeno}")
    else:
        print(f"Tvoje název je {jmeno}")

pozdrav("Albert")
pozdrav("Anna")
pozdrav("Šimon")


def umocneni(cislo_k_umocnení, mocnina=2):
    print(f"{cislo_k_umocnení} ** {mocnina} je {cislo_k_umocnení**mocnina}")

umocneni(2,2)
umocneni(2,3)
umocneni(3,2)

umocneni(4)
umocneni(4,3)
umocneni(4, mocnina=3)

def print_jmena(jmeno="Karel", prijmeni:str="Ctvrty", vek:int=25, bydliste="Praha"):
    print(f"Jméno: {jmeno}, Přijmení: {prijmeni} věk {vek} bydliste {bydliste}")

print_jmena("Vašek", "Průša")
print_jmena("Průša","Vašek")
print_jmena(prijmeni="Průša", jmeno="Vašek")
print_jmena("Vašek", prijmeni="Průša", bydliste="Brno", vek=30)

def nekonecny_soucet(*args):
    suma = 0
    for n in args: #1,22,3,4,5,10
        suma += n

    return suma


soucet = nekonecny_soucet(1,22,3,4,5,10)
print(soucet)








