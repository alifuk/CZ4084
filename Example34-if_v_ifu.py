

if int("6") > 4:
    print("6 je větší než 4")

if int(input()) > 4:
    print("6 je větší než 4")

#"Dítě", pokud je věk menší než 12 let,
#"Teenager", pokud je věk od 12 do 18 let,
#"Dospělý", pokud je věk od 19 do 59 let,
#"Senior", pokud je věk 60 a více let.

# Ukázka zbytečně komplikovaného kodu.
vek = 10
if vek > 60:
    print("Senior")
else:
    if vek > 19:
        print("Dospělý")
    else:
        if vek >12:
            print("Teenager")
        else:
            print("Dítě")

