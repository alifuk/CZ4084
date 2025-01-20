
def secti(a,b):
    return a+b

def rozdil(a,b):
    return a-b

#print(rozdil(2,3))


moje_funkce = rozdil
print(moje_funkce(2,3))
print(rozdil(2,3))
print(2-3)
print(-1)

def pust_funkci_s_parametry(funkci):
    return funkci(2,3)

print(pust_funkci_s_parametry(rozdil))


def get_math_op(znamenko):
    if znamenko == "+":
        return secti
    elif znamenko == "-":
        return  rozdil

print(get_math_op("+")(4,7))
print(secti(4,7))



def scitani_nebo_odcitani(funkce1, funkce2, a, b):
    if a > b:
        return funkce1
    else:
        return funkce2

nejaka_fuknce = scitani_nebo_odcitani(secti, rozdil, 2,3)
nejaka_fuknce = rozdil
print(nejaka_fuknce(5,9))


