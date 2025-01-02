text_v_souboru = ""

#Ukázka otevření a přečtení souboru
with open("./README.md", "r", encoding="utf-8") as file:
    text_v_souboru = file.readlines()
    for line in file.readlines():
        print(line, end="")
    print("Dokončeno čtení")

#Ukázka připsání textu na konec souboru
with open("./README.md", "a", encoding="utf-8") as file:
    file.write("AHOJ SVĚTE\n")

# Ukázka vytvoření a přepsání celého souboru
with open("./README.md", "w", encoding="utf-8") as file:
    file.write("AHOJ")






    
    