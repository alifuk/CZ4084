import csv

#Uložení do csv souboru
with open("employees.csv", 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Anna Dylan", 2500])
    writer.writerow(["Karel Hubert", 22300])
    writer.writerow(["Robert Kubert", 800])

#Načtení z csv souboru
with open("employees.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)

print("csv.list_dialects()")
print(csv.list_dialects())


