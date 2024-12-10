contacts = {
    "Alice": {"email": "alice@example.com", "phone": "555-1234"},
    "Bob": {"email": "bob@example.com", "phone": "555-5678"},
    "Charlie": {"email": "charlie@example.com", "phone": "555-9101"},
    "Diana": {"email": "diana@example.com", "phone": "555-3456"}
}
#pomocí .get() získejte telefon na Charlieho. Pokud telefon neexistuje, vypište
#'Číslo není v záznamu'
print(contacts.get("Charlie", {}).get("phone", "Číslo není v záznamu"))

#smažte "Charlie" z kontaktů
del contacts["Charlie"]
#použijte úplně stejný kód jako na řádku 9. Program nesmí vypsat chybu
print(contacts.get("Charlie", {}).get("phone", "Číslo není v záznamu"))

#Dianě smažte telefon, ale email jí ponechejte
#del contacts["Diana"]["phone"] #možnost 1
#del contacts.get("Diana")["phone"] #možnost 2
#contacts.get("Diana").pop("phone") #možnost 3
print(f'Mažeme: {contacts["Diana"].pop("phone")}') #možnost 4
print(contacts)