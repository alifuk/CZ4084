#pomocí while cyklu dejte do listu čísla od 1 do 20
#list vyprintujte

cisla = []
while len(cisla) < 20:
    cisla.append(len(cisla) +1)
print(cisla)

#Alternativa
cisla = []
cislo = 1
while cislo < 21:
    cisla.append(cislo)
    cislo += 1
print(cisla)

#Alternativa
cisla = []
cislo = 20
while cislo > 0:
    cisla.append(cislo)
    cislo = cislo - 1
cisla.sort()
print(cisla)