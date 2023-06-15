class Osoba:
 def __init__(self, jmeno, prijmeni, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo

 def __str__(self):
        return f'{self.jmeno} \t {self.prijmeni} \t {self.tel_cislo}'