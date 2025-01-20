class Bankovni_ucet:
    def __init__(self):
        self.__zustatek = 0

    @property
    def zustatek(self):
        self.__zustatek -= 10 #Při každém přístupu k zůstatku odebereme 10 kč.
        if "tajne_heslo" == input("Zadej heslo:"):
            return self.__zustatek
        else:
            return "Chybné heslo"

    @zustatek.setter
    def zustatek(self, nova_hodnota):
        if type(nova_hodnota) == int:
            self.__zustatek = nova_hodnota

karta = Bankovni_ucet()
karta.zustatek = "AHoj"
print(karta.zustatek)
print(karta.zustatek)
print(karta.zustatek)
