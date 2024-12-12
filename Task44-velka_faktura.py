faktury_k_vystaveni = [
    ["Panasonic", 30000, "Martin Novotný"],
    ["Oracle", 22000, "Petr Lukoš"],
    ["Porsche", 32345, "Ivo Gira"],
    ["Siemens", 2000, "Luboš Šejk"],
]
ico_moji_firmy = 3456785
#Faktura ID 0. Vystavuje firma 3456785. Faktura pro Martin Novotný na částku 30000 pro firmu Panasonic
for index, faktura in enumerate(faktury_k_vystaveni):
    firma = faktura[0]
    castka = faktura[1]
    jmeno = faktura[2]
    print(f"Faktura ID {index}. Vystavuje firma {ico_moji_firmy}"
          f". Faktura pro {jmeno} na částku {castka} pro firmu {firma}")

#Řešní při použití indexování
print("Řešní při použití indexování")
for i, _ in enumerate(faktury_k_vystaveni):
    print(i)
    ico = ico_moji_firmy
    jme = faktury_k_vystaveni[i][2]
    cas = faktury_k_vystaveni[i][1]
    fir = faktury_k_vystaveni[i][0]
    print(f"Faktura ID {i}. Vystavuje firma {ico}. Faktura pro {jme} na částku {cas} pro firmu {fir}")


#Automatické rozbalení tuplu
clovek = ("Aleš", 33, "Programátor")
jmeno, vek, prace = clovek
print(f"{jmeno}, {vek}, {prace}")