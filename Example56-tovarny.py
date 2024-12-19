class Tovarna:
    def __init__(self, nazev):
        self.nazev = nazev
        self.pocet_zamestnancu = 0
        self.knowhow = []

    def nastavit_pocet_zamestnancu(self, novy_pocet):
        if novy_pocet < 0:
            print("Toto není možné, přiřazení nevykonám")
        else:
            self.pocet_zamestnancu = novy_pocet

    def pridat_HR_oddeleni(self):
        self.pocet_zamestnancu += 4

    def pridat_smenu(self):
        self.pocet_zamestnancu += 30

    def vymenit_knownow(self, jina_tovarna ):
        self.knowhow.extend(jina_tovarna.knowhow)
        pass

rolex = Tovarna("Rolex")
rolex.nastavit_pocet_zamestnancu(40)
rolex.pridat_HR_oddeleni()
rolex.pridat_smenu()
rolex.pridat_smenu()
rolex.knowhow.append("cistota")
print(f"Továrna na {rolex.nazev} má {rolex.pocet_zamestnancu} zaměstnanců")
ikea = Tovarna("Ikea")
ikea.pridat_smenu()
ikea.knowhow.append("preciznost")
rolex.vymenit_knownow(ikea)
print(f"Továrna {rolex.nazev} má knowhow {rolex.knowhow}")