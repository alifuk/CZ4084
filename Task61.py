#Úkol na procvičení ifů a práce se soubory.

#Program se nás zeptá, zdali chceme číst soubor, připrat k souboru
# nebo vytvořit nový soubor/přepsat
volba = input("Zvol (cist, pripsat, zapsat):")
#Pokud uživatel zvolí "cist" tak se nás program zeptá jaký soubor chceme přečíst a
#obsah tohoto souboru vypíšeme do konzole
if volba == "cist":
    nazev_souboru = input("Zadej název souboru ke čtení")
    with open(nazev_souboru, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line, end="")
#Pokud zvolíme "pripsat", zeptá se nás program k jakému souboru chceme připisovat a následně co chceme připsat
elif volba == "pripsat":
    nazev_souboru = input("Zadej název souboru k připsání")
    co_pripsat = input("Zadej co chceš připsat")
    with open(nazev_souboru, "a", encoding="utf-8") as file:
        file.write(f"{co_pripsat}\n")
#Pokud uživatel zvoli "zapsat", tak se nás progrgma jaký soubor chceme zapisovat a následně co chceme zapsat
else:
    nazev_souboru = input("Zadej název souboru k zapsání")
    co_zapsat = input("Zadej co chceš zapsat")
    with open(nazev_souboru, "w", encoding="utf-8") as file:
        file.write(f"{co_zapsat}")

#import os
#print(os.getcwd()) #vypíše cestu k aktuálnímu adresáři
#print(os.listdir(".")) #vypíše vše v aktuálnim adresáři