
class Auto:
    def __init__(self, brand, type, price):
        self.brand = brand
        self.type = type
        self.price = price

    def zvysit_cenu(self, o_kolik_zvysit):
        self.price += o_kolik_zvysit

    def printit(self):
        print(f"Auto {self.brand} model {self.type} stojí {self.price}")


ferrari = Auto("Ferrari", "California", 300000)
ferrari.zvysit_cenu(20000)
ferrari.printit() #Auto Ferrari model California stojí 320000

audi = Auto("Audi", "A4", 40000)
audi.zvysit_cenu(-30000)
audi.printit() #Auto Audi model A4 stojí 10000


