platby = [3000, 200, 18, 34444]
#ke každý platbě vypíšeme fakturu
ICO = 3455432
#Vystavuji fakturu ID 0 od firmy s IČO 3455432 na částku 3000
#Vystavuji fakturu ID 1 od firmy s IČO 3455432 na částku 200
#Vystavuji fakturu ID 2 od firmy s IČO 3455432 na částku 18
#Vystavuji fakturu ID 3 od firmy s IČO 3455432 na částku 34444
#pomocí for cyklu a enumerate()
for index, castka in enumerate(platby):
    print(f"Vystavuji fakturu ID {index} od firmy s IČO {ICO} na částku {castka}")
