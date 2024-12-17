#Trénink dělení čísel.
#Na začátku programu vygenerujte čísla 'a' a 'b', které jsou 0-100
#ve while cyklu se uživatele ptejte, kolik je a//b. pokud uživatel odpoví špatně, tak se while cyklus vykoná znovu
#tzn. dokud úlohu uživatel nevyřeší správně, tak program neskončí.

#tipy:
import random
a = random.randint(0,100) #toto vrátí náhodné číslo
b = random.randint(1, 100)
print(f"Kolik je {a}//{b}? Zadej odpověď:")
#nezapomenout, že int(input())
#Varianta 1

while True:
    vstup_od_uzivatele = int(input())
    if vstup_od_uzivatele == a//b:
        break
    print("To není pravda")
print("Gratuluji")

#Varianta 2
nevyreseno = True
while nevyreseno:
    if int(input()) == a//b:
        nevyreseno = False
print("Gratuluji k vyřešení")