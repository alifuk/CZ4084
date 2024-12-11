vek = 7
print(f"Je ti {vek} let")
if vek >= 18:  # > < >= <= ==
    print("Jsi dospělý1")
    print("Jsi dospělý2")
    print("Jsi dospělý3")
    print("Jsi dospělý4")
if vek < 18:
    print("Nejsi dospělý")
#Alternativní zápis je:
if vek >= 18:
    print("Jsi dospělý1")
else:
    print("Nejsi dospělý")

#Pokud chceme více podmínek:
if vek > 18:
    print("Jsi dospělý")
elif vek == 18:
    print(f"Gratuluji, právě ti bylo 18")
else:
    print("Nejsi dospělý")

#Předloha zápisu
if True :
    print("Toto se vždy vykoná")

if False :
    print("Toto se nikdy nevykoná")

#Jak převést text na číslo
cislo = int("18")
print(cislo)




