jmena = ["Jura", ["Eliška"], "Katka"] #Tento řádek neupravujte
#pomocí příkazu .insert() rozšiřte jmena, tak aby obsahovala:
# ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
jmena[1].insert(1, "Ruda")
jmena.insert(2, "Božka")
jmena.insert(4, ["Michal", "Liza"])

#   ŘÁDKY níže neupravujte
vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {jmena}, ale mělo vyjít {vsechny_jmena} "
print("Gratuluji")



