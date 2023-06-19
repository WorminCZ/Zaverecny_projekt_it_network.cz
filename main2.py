from osoba import Osoba #import třídy Osoba, která se stará o samotné osoby
from pojisteni import Pojisteni #import třídy Pojištění, která se stará o funkce databáze
import datetime #import knihovny datetime, kterou používáme ke "zpestření" úvodu

"""
-------------------------------------------------------------------------------
             Databáze pojištěnců - závěrečný projekt ITnetwork.cz
                               Jaroslav Totušek
-------------------------------------------------------------------------------
"""

now = datetime.datetime.now() # Při výpisu času chceme pracovat s aktuálním časem
pojisteni = Pojisteni() # Z classy pojištění vytváříme konkrétní instanci, ergo vytváříme seznam na pojištěnce

def dotaz_na_pokracovani(): # Funkce, která za nás vyřeší dotazování se v aplikaci.
     while True:
        user_input = input("Chcete pokračovat? ano/ne: \n")
        if user_input.lower() == "ano":  # Inputy převádíme na malá písmena, kdyby náhodou uživatel někde použil velká
            # Pokračovat od začátku
            break
        elif user_input.lower() == "ne":
            # Ukončit program
            print("Program se ukončí. Děkujeme za využití databáze.")
            exit()
        else:
            print("Tento příkaz neznám. Zadejte prosím 'ano' nebo 'ne'.")

print(f"\n********\nVítejte v evidenci pojištěnců! Dnes je {now.day}.{now.month}.{now.year}\n********\n\n"
                  "Prosím, vyberte, co chcete dělat: \n"
                  "Přidat nového pojištěného - 1\n"
                  "Vypsat pojištěné - 2\n"
                  "Vyhledat konkrétního pojištěnce - 3\n"
                  "Ukončit aplikaci - 4\n\n")

volba = int(input("Zadejte možnost:  "))

if volba == 1: # Přidávání pojištěnců
    jmeno = input("Vyplňte křestní jméno pojištěnce:\n")
    prijmeni = input("Vyplňte příjmení pojištěnce:\n")
    tel_cislo = int(input("Zadejte telefonní číslo pojištěnce (bez mezer):\n"))
    osoba = Osoba(jmeno,prijmeni,tel_cislo)
    pojisteni.pridej(osoba) # Přidáváme instanci osoba se vstupními argumenty do seznamu
    print(f"Do systému byl zadán pojištěnec {jmeno} {prijmeni} s telefonním číslem: {tel_cislo}")
    dotaz_na_pokracovani()

elif volba == 2: # Výpis pojištěnců ze seznamu
   pojisteni.vypis()
   dotaz_na_pokracovani()


elif volba == 3: # Hledání pojištěnců
     zadane_jmeno = input("Zadejte jméno: ")
     zadane_prijmeni = input("Zadejte příjmení: ")
     pojisteny = pojisteni.najdi(zadane_jmeno, zadane_prijmeni)
     if pojisteny:
         print(f"Pojištěnec nalezen. {zadane_jmeno} {zadane_prijmeni} je v databázi.")
     else:
         print("Pojištěnec nebyl nalezen")
     dotaz_na_pokracovani()

elif volba == 4: # Konec programu
     print("Program se ukončí. Děkujeme za využití databáze.")
     exit()

else: # Ošetření neznámého vstupu
     print("Tuto možnost program nezná.")
     dotaz_na_pokracovani()
