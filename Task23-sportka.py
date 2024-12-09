sportka = [3,5,8,1] #Nesahat
#Použijte příkaz insert, sort, reverse a pop, a získejte [8, 4, 3, 1]

sportka.insert(2,4)
sportka.sort()
sportka.reverse()
sportka.pop(1)

assert [8, 4, 3, 1] == sportka, f"Má vyjít [8, 4, 3, 1] a vyšlo {sportka}"
print("Výhra!!!!")

