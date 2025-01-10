import random

class Lokace:
    def __init__(self, jmeno, ceny):
        self.jmeno = jmeno
        self.ceny = ceny  # Slovník s cenami předmětů

    def aktualizuj_ceny(self):
        for predmet in self.ceny:
            zmena = random.randint(-5, 5)
            nova_cena = self.ceny[predmet] + zmena
            self.ceny[predmet] = max(predmet.min_cena, min(predmet.max_cena, nova_cena))

    def __str__(self):
        return self.jmeno