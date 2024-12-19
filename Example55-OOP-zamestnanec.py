
class Zamestnanec:
    def __init__(self, jmeno, prijmeni, plat):
        self.jmeno = jmeno
        self.plat = plat
        self.prijmeni = prijmeni

    def pridat_plat(self, navyseni_platu):
        self.plat += navyseni_platu

    def printit(self):
        print(f"Zaměstnanec {self.jmeno} příjmením {self.prijmeni} má plat {self.plat} Kč")

petr = Zamestnanec("Petr", "Novák", 60000)
petr.pridat_plat(5000)
petr.printit() #Zaměstnanec Petr příjmením Novák má plat 65000 Kč

lenka = Zamestnanec("Lenka", "Nováková", 55000)
lenka.pridat_plat(11000)
lenka.printit() #Zaměstnanec Lenka příjmením Nováková má plat 66000 Kč