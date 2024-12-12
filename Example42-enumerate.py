fruits = ["jablko", "banán", "citrón"]

for index, fruit in enumerate(fruits):
    print(f"Druh ovoce: {fruit}, na indexu: {index}.")

for cislo_od_nuly, ovoce in enumerate(fruits):
    print(f"Druh ovoce: {ovoce}, na indexu: {cislo_od_nuly}.")

print("Ekvivalent enumerate jen pro tento příklad")
for cislo_od_nuly, ovoce in [[0,"jablko"], [1,"banán"], [2,"citrón"]]:
    print(f"Druh ovoce: {ovoce}, na indexu: {cislo_od_nuly}.")

print("kdybych to prohodil")
for cislo_od_nuly, ovoce in [["jablko", 0], ["banán",1], ["citrón",2]]:
    print(f"Druh ovoce: {ovoce}, na indexu: {cislo_od_nuly}.")

'''
for ovoce, cislo_od_nuly  in enumerate(fruits): #POZOR!!! V PROMENNÉ ovoce BUDOU INDEXY
    print(f"Druh ovoce: {ovoce}, na indexu: {cislo_od_nuly}.")
'''