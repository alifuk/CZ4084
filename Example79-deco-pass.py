import hashlib

def pod_heslem(fnc):
    def zaheslovano():
        zadane_heslo = input("Zadej heslo:")
        if str(hashlib.md5(zadane_heslo.encode()).hexdigest()) == "07871915a8107172b3b5dc15a6574ad3":
            fnc()
        else:
            print("Špatné heslo, žádné jídlo nemáme")
    return zaheslovano

def basic_jidlo():
    print("Tady máš hamburgr")

@pod_heslem
def premium_jidlo():
    print("Tady máš lasagne")

vstup = input("Jaké chceš jídlo? (b/p)")
if vstup == "b":
    basic_jidlo()
elif vstup == "p":
    premium_jidlo()




