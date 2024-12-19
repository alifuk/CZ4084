zvirata = []
class Zvire():
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.krmeno = False

    def vypis_zvire(self):
        if self.krmeno:
            print(f"Jméno: {self.jmeno} má {self.vek} let. A dnes bylo krmeno.")
        else:
            print(f"Jméno: {self.jmeno} má {self.vek} let. Potřeba nakrmit.")

    def nakrmit(self):
        self.krmeno = True
        print(f"Bylo nakrmeno zvíře {self.jmeno}")

def vypsat_vsechny():
    for zvire in zvirata:
        if zvire.krmeno:
            print(f"Jméno: {zvire.jmeno} má {zvire.vek} let. A dnes bylo krmeno.")
        else:
            print(f"Jméno: {zvire.jmeno} má {zvire.vek} let. Potřeba nakrmit.")

def nakrmit(jmeno_zvirete_k_nakrmeni):
    for zvire in zvirata:
        if zvire.jmeno == jmeno_zvirete_k_nakrmeni:
            zvire.nakrmit()

def spocitat():
    print(f"Máme {len(zvirata)} zvířat")

def odebrat(jmeno_zvirete_k_odebrani):
    global zvirata
    nova_zvirata = []
    for zvire in zvirata:
        if zvire.jmeno != jmeno_zvirete_k_odebrani:
            nova_zvirata.append(zvire)
    zvirata = nova_zvirata

while True:
    print("Možné příkazy:")
    print("1-pridat")
    print("2-vypsat_vsechny")
    print("3-konec")
    print("4-nakrmit")
    print("5-spocitat")
    print("6-odebrat")
    prikaz = input("Zadejte prikaz:")
    if prikaz == "pridat" or prikaz == "1":
        jmeno = input("Jmeno?")
        vek = int(input("Věk?"))
        zvirata.append(Zvire(jmeno,vek))
    elif prikaz == "vypsat_vsechny" or prikaz == "2":
        vypsat_vsechny()
    elif prikaz == "konec" or prikaz == "3":
        break
    elif prikaz == "nakrmit" or prikaz == "4":
        jmeno_zvirete = input("Jaké zvíře chcete nakrmit?")
        nakrmit(jmeno_zvirete)
    elif prikaz == "spocitat" or prikaz == "5":
        spocitat()
    elif prikaz == "odebrat" or prikaz == "6":
        jmeno_zvirete = input("Jaké zvíře chcete odebrat?")
        odebrat(jmeno_zvirete)
    else:
        print(f"Neznámý příkaz {prikaz}")
print("Děkuji za použití programu")





