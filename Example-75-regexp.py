import re

#print(re.search(r"[A-Z]la", "ala Ola Ela"))

#print(re.findall(r"[A-Z]\w*", "Albert jede na kole značky Favorit"))

veta = "Albert-jede-na-kole-značky-Favorit"
slova = veta.split("n")
print(slova)

print(re.split(r",|\.", "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"))

print(veta.replace("Favorit", "Mikono"))