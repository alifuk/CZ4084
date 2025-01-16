# Zadání

Ve světě tohoto programu existují různé typy bankovních účtů, každý s jinými pravidly. Vaším úkolem je implementovat základní logiku účtů pomocí objektově orientovaného programování v Pythonu.

## Abstraktní třída: Account

Tato třída slouží jako základ pro všechny typy účtů.
### Metody:
- deposit(amount: float): Abstraktní metoda pro vklad peněz.
- withdraw(amount: float): Abstraktní metoda pro výběr peněz.
- get_balance() -> float: Vrací aktuální zůstatek na účtu.
### Properties:
- balance: float: Aktuální zůstatek účtu.
- account_number: str: Číslo účtu (při vytvoření účtu se vygeneruje).

## Třída SavingsAccount (dědí Account)

 Spořící účet, který neumožňuje přečerpání.
### Metody:
- deposit(amount: float): Přidá peníze na účet.
- withdraw(amount: float): Povolí výběr, pokud je na účtu dostatek peněz. Jinak vyvolá výjimku.
- apply_interest(): Přičte úrok ke zůstatku.
### Properties:
- interest_rate: float: Roční úroková míra.

## Třída CheckingAccount (dědí Account)

Běžný účet, který umožňuje přečerpání až do určitého limitu.
### Properties:
- overdraft_limit: float: Maximální povolené přečerpání.
### Metody:
- deposit(amount: float): Přidá peníze na účet.
- withdraw(amount: float): Umožní výběr, pokud zůstatek po výběru nepřesáhne povolený limit přečerpání. Jinak vyvolá výjimku.

## Vlastní výjimky

- InsufficientFundsError: Vyvolá se při pokusu o výběr větší částky, než je na účtu (nebo pokud je přečerpání nad limitem).
- InvalidAmountError: Vyvolá se při pokusu vložit nebo vybrat zápornou částku.

```
#Vytvoření účtů
savings = SavingsAccount("123456", interest_rate=0.03)
checking = CheckingAccount("654321", overdraft_limit=500)

#Práce s účty
savings.deposit(1000)
savings.apply_interest()

checking.deposit(500)
try:
    checking.withdraw(1200)  # Toto vyvolá výjimku
except InsufficientFundsError as e:
    print(e)

print(savings.get_balance())  
print(checking.get_balance())  
```
