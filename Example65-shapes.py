from abc import ABC, abstractmethod

platno = [] #vytvoření plátna 8x8 znaků
for i in range(8):
    radek = []
    for j in range(8):
        radek.append(".")
    platno.append(radek)


class Tvar(ABC):
    @abstractmethod
    def vykresli(self, platno):
        pass


class Obdelnik(Tvar):
    def vykresli(self, platno):
        pass

class Ctvrec(Tvar):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def vykresli(self, platno):
        velikost = 2
        for radek in range(velikost):
            for sloupec in range(velikost):
                platno[radek+self.y][sloupec+self.x] = "C"

class Kruh(Tvar):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def vykresli(self, platno):
        for radek, znaky_v_radku in enumerate(platno):
            for sloupec, _ in enumerate(znaky_v_radku):
                vzdalenost = abs(self.x - sloupec) + abs(self.y - radek)
                if vzdalenost < 3:
                    platno[radek][sloupec] = "K"


tvary = [Ctvrec(3,3), Ctvrec(2,1), Kruh(3,5), Obdelnik()]
for tvar in tvary:
    tvar.vykresli(platno)

#vykreslení plátna
for radek in platno:
    for znak in radek:
        print(znak, end="")
    print()