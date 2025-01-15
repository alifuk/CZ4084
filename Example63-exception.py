
try:
    print(2/0)
except Exception as e:
    print(e)
    print("Nastala vyjímka")
finally:
    print("finally")

try:
    raise Exception("NASTALA CHYBA")
except Exception as e:
    print(e)

print("Hotovo")


