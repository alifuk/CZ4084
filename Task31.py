'''
Zadání:
Napiš program, který požádá uživatele o zadání věku.
Program zkontroluje a vypíše, do které věkové kategorie patří:

"Dítě", pokud je věk menší než 12 let,
"Teenager", pokud je věk od 12 do 18 let,
"Dospělý", pokud je věk od 19 do 59 let,
"Senior", pokud je věk 60 a více let.
'''

vek = int(input("Zadej věk"))
if vek < 12:
    print("Dítě")
elif vek < 20:
    print("Teen")
elif vek < 60:
    print("Dospělý")
else:
    print("Senior")

