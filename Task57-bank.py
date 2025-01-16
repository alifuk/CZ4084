class Banka:
    def __init__(self, jmeno):
        #třída Banka bude mít atribut jmeno a
        # zustatek (počáteční zůstatek je 0)
        self.jmeno = jmeno
        self.zustatek = 0
        pass

    def vklad(self, castka):
        #vložení částky k zůstatku
        print(f"Zůstatek na účtu před vkladem {self.zustatek}")
        self.zustatek += castka
        print(f"Zůstatek na účtu po vkladu {self.zustatek}")
        pass

    def vyber(self, castka):
        if castka <= self.zustatek:
            self.zustatek -= castka
            print("Vybráno")
        else:
            print("Nelze vybrat!!!")
        #částka se odebere ze zůstatku
        pass

    def __repr__(self):
        return f"Zůstatek na účtu {self.jmeno} je {self.zustatek} Kč"

#Vytvořte instanci třídy Banka
mmkarta = Banka("Firma MM")
#Vložte 20000
mmkarta.vklad(20000)
#Vyberte 4000
mmkarta.vyber(4000)
#vyprintujte zůstatek a jméno
print(mmkarta)


