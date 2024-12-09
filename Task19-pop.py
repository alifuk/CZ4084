vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .pop(index) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]
vsechny_jmena[1].pop(1) #Ruda
vsechny_jmena.pop(2) #Božka
vsechny_jmena.pop(3) #["Michal", "Liza"]
#   ŘÁDKY níže neupravujte
jmena = ["Jura", ["Eliška"], "Katka"]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")