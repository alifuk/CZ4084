
cislo = 1
while cislo < 10:
    print(cislo)
    cislo += 1
print("Dokončeno")

#Dvakrát while v sobě s if
mocniny = {}
zaklad = 1
while zaklad < 7:
    mocniny[zaklad] = 1
    kolikrat_budeme_nasobit = zaklad
    while kolikrat_budeme_nasobit > 0:
        mocniny[zaklad] *= kolikrat_budeme_nasobit
        kolikrat_budeme_nasobit -= 1
        if mocniny[zaklad] > 100:
            print(f"Toto už je velké číslo {mocniny[zaklad]}")
    zaklad += 1
print(mocniny)










