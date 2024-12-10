#tuple
domaci_spotrebice = ("Lednice", "Pračka", "Myčka")
print(domaci_spotrebice[2])
#domaci_spotrebice.append("Trouba") #NELZE
#domaci_spotrebice[1] = "Konvice" #Nelze

#set
zvirata = {"Delfín", "Myš", "Žirafa"}
print(zvirata)
zvirata.add("Slon")
print(zvirata)
zvirata.add("Slon")
zvirata.update(["Slon", "Lev", "Papoušek"])
print(zvirata)

zoo = set()
print(f"Zoo: {zoo}")
zoo.add("Had")
print(f"Zoo: {zoo}")

kanalizace = set(["myš", "myš", "potkan", "myš"])
print(kanalizace)
kanalizace.remove("myš")
#kanalizace.remove("brouk") #NASTANE CHYBA, PROTOŽE brouk NENÍ V kanalizace
kanalizace.discard("brouk")




