#Chceme vykreslit pyramidu

#
##
###
####

radek = 1
while radek < 5:
    sloupec = 0
    co_vypsat = ""
    while sloupec < radek:
        co_vypsat += "#"
        sloupec += 1
    print(co_vypsat)
    radek += 1