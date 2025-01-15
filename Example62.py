import Task61

if __name__ == "__main__": #pouze pokud jsme spouštěli přímo tento soubor
    print("AHA")

suda_cisla = [x for x in range(10) if x %2 == 0]
print(suda_cisla)



vek = 18
ma_penez = 80
if vek >= 18 and ma_penez >= 100:
    print("jsi dospely")




#dict
auta = {"Skoda":"ČR", "Porsche":"DE"}

#set
staty = {"ČR", "DE"}

#tuple
dvojice = ("L", "P")

#list
pismena = ["A", "A", "B", "C", "D"]




print("A" in ["A", "B", "C", "D"])
print("q" in "Albert")
#▼╬▼╬▼╬▼╬▼╬▼╬▼╬▼╬▼╬


#print("3" + 3)

#print([2,3,4][20])

def soucet(a,b):
    return a+b

print(soucet(3,4) + soucet(5,6))
print(7 + 11)
print(18)


for i in range(12):
    if i % 2 == 0: #sudé číslo
        continue
    print(i)


print(True and False)    #False
print(False or False)     #False
print(False or True)     #True
print(False or True and False)     #False


number = int(input("Zadej číslo:"))

print(number, end="TOTO je konec řádku\n")
