class Pojisteni:
    def __init__(self):
        self.pojisteni_seznam = []

    def pridej(self, osoba):
        self.pojisteni_seznam.append(osoba)

    def najdi(self, jmeno, prijmeni):
        for pojisteni in self.pojisteni_seznam:
            if pojisteni.jmeno == jmeno and pojisteni.prijmeni == prijmeni:
                return pojisteni

    def vypis(self):
        if not self.pojisteni_seznam :
            print("Seznam pojištěnců je prázdný.")
        else:
            for osoba in self.pojisteni_seznam:
                print(osoba)
