from Obchodnik.Lokace import Lokace
from Obchodnik.Predmet import Predmet
from Obchodnik.Osoba import Osoba

# Předměty
utopenec = Predmet("Utopenec", 50, 100)
med = Predmet("Med", 150, 300)
palava = Predmet("Láhev Pálavy", 250, 500)

predmety = [utopenec, med, palava]

# Lokace s pevnými cenami
hradcany = Lokace("Hradčany", {utopenec: 50, med: 200, palava: 400})
vaclavak = Lokace("Václavák", {utopenec: 70, med: 140, palava: 250})
holesovice = Lokace("Holešovice", {utopenec: 90, med: 190, palava: 320})

lokace = [hradcany, vaclavak, holesovice]

# Vytvoření hráče
hrac = Osoba("Hráč", 100)

# Základní smyčka hry
aktualni_lokace = hradcany

print("Vítejte ve hře!")
while not hrac.je_konec_hry():
    print(f"\nAktuální lokace: {aktualni_lokace}")
    print(f"Dny: {hrac.dny}, Peníze: {hrac.penize} Kč")
    print("Vaše inventář:")
    for predmet, mnozstvi in hrac.inventar.items():
        print(f"- {predmet.jmeno}: {mnozstvi} ks")

    print("Předměty k prodeji/nákupu:")
    for predmet, cena in aktualni_lokace.ceny.items():
        print(f"- {predmet.jmeno}: {cena} Kč")

    print("Možnosti:")
    print("1. Přesun do jiné lokace")
    print("2. Koupit předmět")
    print("3. Prodat předmět")

    try:
        volba = int(input("Zvolte akci: "))

        if volba == 1:
            print("Lokace na výběr:")
            for i, lok in enumerate(lokace):
                print(f"{i + 1}. {lok}")

            volba_lokace = int(input("Vyberte číslo lokace: ")) - 1
            if 0 <= volba_lokace < len(lokace):
                aktualni_lokace = lokace[volba_lokace]
                hrac.presun_do_lokace(aktualni_lokace)
            else:
                print("Neplatná volba.")

        elif volba == 2:
            print("Předměty k nákupu:")
            for i, (predmet, cena) in enumerate(aktualni_lokace.ceny.items()):
                print(f"{i + 1}. {predmet.jmeno}: {cena} Kč")

            volba_predmet = int(input("Vyberte číslo předmětu: ")) - 1
            if 0 <= volba_predmet < len(predmety):
                predmet = predmety[volba_predmet]
                hrac.koupit(predmet, aktualni_lokace.ceny[predmet])
            else:
                print("Neplatná volba.")

        elif volba == 3:
            print("Předměty k prodeji:")
            for i, (predmet, mnozstvi) in enumerate(hrac.inventar.items()):
                if mnozstvi > 0:
                    print(f"{i + 1}. {predmet.jmeno}: {mnozstvi} ks (Cena: {aktualni_lokace.ceny[predmet]} Kč)")

            volba_predmet = int(input("Vyberte číslo předmětu: ")) - 1
            if 0 <= volba_predmet < len(predmety):
                predmet = predmety[volba_predmet]
                hrac.prodat(predmet, aktualni_lokace.ceny[predmet])
            else:
                print("Neplatná volba.")

        else:
            print("Neplatná volba.")

    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")

print(f"\nHra skončila! Celkový počet dnů: {hrac.dny}, Zůstatek: {hrac.penize} Kč.")
