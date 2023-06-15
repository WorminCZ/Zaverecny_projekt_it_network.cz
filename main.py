from osoba import Osoba #import třídy Osoba, která se stará o samotné osoby
from pojisteni import Pojisteni #import třídy Pojištění, která se stará o funkce databáze
import datetime #import knihovny datetime, kterou používáme ke "zpestření" úvodu

"""
-------------------------------------------------------------------------------
             Databáze pojištěnců - závěrečný projekt ITnetwork.cz
                               Jaroslav Totušek
-------------------------------------------------------------------------------
"""

now = datetime.datetime.now() #Při výpisu času chceme pracovat s aktuálním časem
pojisteni = Pojisteni() #Z classy pojištění vytváříme konkrétní instanci, ergo vytváříme seznam na pojištěnce

print(f"\n********\nVítejte v evidenci pojištěnců! Dnes je {now.day}.{now.month}.{now.year}\n********\n\n"
                  "Prosím, vyberte, co chcete dělat: \n"
                  "Přidat nového pojištěného - 1\n"
                  "Vypsat pojištěné - 2\n"
                  "Vyhledat konkrétního pojištěnce - 3\n"
                  "Ukončit aplikaci - 4\n\n")

dalsi = "ano"
while dalsi == "ano":
 volba =  int(input("Zadejte možnost:  "))

 if volba == 1:
    jmeno = input("Vyplňte křestní jméno pojištěnce:\n")
    prijmeni = input("Vyplňte příjmení pojištěnce:\n")
    tel_cislo = int(input("Zadejte telefonní číslo pojištěnce:\n"))
    osoba = Osoba(jmeno,prijmeni,tel_cislo)
    pojisteni.pridej(osoba)
    print(f"Do systému byl zadán pojištěnec {jmeno} {prijmeni} s telefonním číslem: {tel_cislo}")

    dalsi = input("Přejete si pokračovat? ano/ne:\n")
    if dalsi == "ano":
        continue
    elif dalsi == "ne":
        break
    else:
        print("Zadáváte nesprávné hodnoty")

 elif volba == 2:
   pojisteni.vypis()

   dalsi = input("Přejete si pokračovat? ano/ne:\n")
   if dalsi == "ano":
     continue
   elif dalsi == "ne":
     break
   else:
     print("Zadáváte nesprávné hodnoty")



 elif volba == 3:
     zadane_jmeno = input("Zadejte jméno: ")
     zadane_prijmeni = input("Zadejte příjmení: ")
     pojisteny = pojisteni.najdi(zadane_jmeno, zadane_prijmeni)
     if pojisteny:
         print("Pojištěnec nalezen")
     else:
         print("Pojištěnec nebyl nalezen")

     dalsi = input("Přejete si pokračovat? ano/ne:\n")
     if dalsi == "ano":
         continue
     elif dalsi == "ne":
         break
     else:
         print("Zadáváte nesprávné hodnoty")

 elif volba == 4:
     print("Program se nyní ukončí")
     break

 else:
     print("Tuto možnost program nezná.")
     dalsi = input("Přejete si pokračovat? ano/ne:\n")

if dalsi == "ne":
  print("Program se ukončí. Děkujeme za využití databáze.")

