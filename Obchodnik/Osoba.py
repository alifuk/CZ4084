
class Osoba:
    def __init__(self, jmeno, penize):
        self.jmeno = jmeno
        self.penize = penize
        self.dny = 0
        self.inventar = {}

    def presun_do_lokace(self, nova_lokace):
        print(f"{self.jmeno} se přesouvá do lokace {nova_lokace}.")
        self.dny += 1
        nova_lokace.aktualizuj_ceny()

    def je_konec_hry(self):
        return self.dny >= 14

    def koupit(self, predmet, cena):
        if self.penize >= cena:
            self.penize -= cena
            if predmet in self.inventar:
                self.inventar[predmet] += 1
            else:
                self.inventar[predmet] = 1
            print(f"Koupili jste {predmet} za {cena} Kč.")
        else:
            print("Nemáte dost peněz!")

    def prodat(self, predmet, cena):
        if predmet in self.inventar and self.inventar[predmet] > 0:
            self.inventar[predmet] -= 1
            self.penize += cena
            print(f"Prodali jste {predmet} za {cena} Kč.")
        else:
            print("Nemáte tento předmět k prodeji!")
