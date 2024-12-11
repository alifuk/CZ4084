#tipovačka pevnýho čísla
import random
vyherni_cislo = random.randint(0,100)
#kod donekonečna vyzývá k zadání čísla.
#po zadání čísla, bude sděleno, sdali je tipnuté číslo větší nebo menší než výherní číslo
#jakmile bude výherní číslo tipnuto, bude vypsáno "Výhra!!!!!"

uhodli_jsme = False
while uhodli_jsme == False:
    tip = int(input("Zadejte cislo"))
    if tip == vyherni_cislo:
        uhodli_jsme = True
    elif tip > vyherni_cislo:
        print("Tipnuto hodně")
    else:
        print("Tipnuto málo")
print("Výhra!!!!!")
