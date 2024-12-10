zlaty_stranky = { #dict / dictionary / slovník
    'Praha': 22222222,
    'CeskaPosta': "Nemáme číslo",
    "Financak": [1,2],
    "OSSZ": {
        "Odbor_dopravy": 33444444,
        "Odbor_okresu": 3444444,
    }
}
#Pokud chci zíkat v dict podklíč v poddictionary, tak použiju:
print(f'Odbor_okresu {zlaty_stranky.get("OSSZ", {}).get("Odbor_okresu", "Neexistuje")}')

print(zlaty_stranky["OSSZ"]["Odbor_dopravy"]) #Pokud klíč "OSSZ" nebo "Odbor_dopravy" neexistuje, tak program spadne

zlaty_stranky["Albert"] = 4444444444 #přidání dalšího klíče s hodnotou
zlaty_stranky["Petra"] = 909087888
zlaty_stranky["klic"] = "hodnota"

print(f'Klíč Odbor_dopravy {zlaty_stranky.get("Odbor_dopravy", "Musíš to najít")}')
print(f'Klíč Albert {zlaty_stranky.get("Albert", "Musíš to najít")}')
del zlaty_stranky["Petra"] #Smazání klíč
zlaty_stranky.pop("klic") #Smazání klíč

print(zlaty_stranky)
