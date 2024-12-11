
slova = []
while True:
    vstup = input("Zadej slovo nebo 'ukoncit': ")
    if vstup == "ukoncit":
        break
    slova.append(vstup)
print(slova)