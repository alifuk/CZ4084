def add_ingredients(**kwargs):
    print(kwargs)
    ingredients_count = 0
    for key in kwargs:
        ingredients_count += kwargs[key]
    return ingredients_count

print(add_ingredients(eggs=2, spam=1, cheese=3))



def print_power(**kwargs):
    for key, value in kwargs.items():
        print(f"Auto {key} má výkon {value}")
print_power(skoda=130, mazda=200, bmw=250)


#Procházení dict

mesta = {
    "praha": 80,
    "brno": 70,
    "ostrava":30
}
print(mesta["ostrava"])
#procházení klíčů
for key in mesta.keys():
    print(f"key: {key}")
#procházení hodnot
for value in mesta.values():
    print(f"value: {value}")
#procházení klíčů i hodnot
for mesto, hodnoceni in mesta.items():
    print(f"key {mesto} value {hodnoceni}")