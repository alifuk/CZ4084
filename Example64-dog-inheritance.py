class Pes:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def udelej_zvuk(self):
        print("Raf")

    def __str__(self):    #__repr__ a __str__ je jedno a to samé
        return f"Haf haf, jsem {self.jmeno}"

class Jezevcik(Pes):
    def __init__(self):
        super().udelej_zvuk()
        super().__init__("Vojta")

vojta = Jezevcik()
print(vojta)
