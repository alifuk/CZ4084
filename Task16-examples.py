'''
.count(x) #vypočte počet výskytů x v listu
.index(x) #chci zjistit na jaké pozici je x. !!!list je indexovaný od 0
.insert(index, x) #vložení prvku x na index
.pop(index) #odebere prvek z daného indexu
.pop() #odebere poslední prvek z pole
.remove(x) #odebere první výskyt prvku x
.clear() #vše smaže z listu
.reverse() #otočí mi list
.sort() #seřadí list
.append(x) #vloží prvek na konec listu
.extend(x) #vloží list x jako jednotlivé prvky
'''

#.count(x)
seznam_jmen = ["Albert", "Alena", "Alfons", "Alena"]
print(f"V seznam_jmen je 'Alena' {seznam_jmen.count('Alena')} krát")

#.index(x)
print(f"'Alfons' je na indexu {seznam_jmen.index('Alfons')}")

#.insert(index,x)
seznam_jmen.insert(1, "Alkapon")
print(seznam_jmen)

#.pop()
odebrany_prvek = seznam_jmen.pop()
print(seznam_jmen)
print(f"Odebrali jsme {odebrany_prvek}")

#.pop(index)
prvek_index_dva = seznam_jmen.pop(2)
print(seznam_jmen)
print(f"Z indexu 2 jsme odebrali: {odebrany_prvek}")

#.remove(x)
seznam_jmen.remove("Albert")
print(f"Po odebrání 'Albert' vypadá seznam jmen takto {seznam_jmen}")
print("-------------------")
seznam = [[3],4, 3,3,3,3]
print(f"Máme list {seznam}")
seznam.remove([3]) #výsledek je [4, 3,3,3,3]
print(f"Výsledek po odebrání [3] je: {seznam}")

seznam = [[3],4, 3,3,3,3]
seznam.remove(3) #výsledek je [[3], 4, 3,3,3]
print(f"Výsledek po odebrání 3 je: {seznam}")

#.clear()
print("---------------")
seznam.clear()
print(f"Po zavolní funkce seznam.clear() vypadá seznam takto: {seznam}")

#.reverse()
seznam_jmen = ["Albert", "Alena", "Alfons"]
seznam_jmen.reverse()
#seznam_jmen = seznam_jmen[::-1]   #dělá to samé to .reverse()
print(f"Otočený seznam jmen je: {seznam_jmen}")

#.sort()
seznam_jmen = ["Robert", "Elena", "Alfons"]
print(f"Máme seznam {seznam_jmen}")
seznam_jmen.sort()
print(f"Seřazený seznam jmen je: {seznam_jmen}")

seznam_cisel = [5,4,8,9,0,2]
print(f"Máme seznam {seznam_cisel}")
seznam_cisel.sort()
print(f"Seřazený seznam čísel od nejmenších je: {seznam_cisel}")
seznam_cisel.sort(reverse=True)
#seznam_cisel = seznam_cisel[::-1]
print(f"Seřazený seznam čísel od největších je: {seznam_cisel}")

#.append(x)
seznam_cisel.append(42)
print(f"Po přidání 42 je seznam_cisel {seznam_cisel}")

#.extend(x)
seznam_cisel.extend([43,45,46])
print(f"Po přidání [43,45,46] je seznam_cisel {seznam_cisel}")



