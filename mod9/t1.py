#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, 
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, 
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#  Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. 
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, 
# huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

import random

class Auto:

    def __init__(self, rek, hn):
        self.rek = rek
        self.hn = hn
        self.vauhti = 0
        self.matka = 0

    def kiihdyta(self, kmh):
        if kmh + self.vauhti <= self.hn and kmh >= 0:
            self.vauhti += kmh
        elif self.vauhti + kmh >= self.hn:
            self.vauhti = self.hn
        return 

    def ebrake(self):
        self.vauhti = self.vauhti - 200
        if self.vauhti < 0:
            self.vauhti = 0
        return

    def kulje(self, aika):
        self.matka = aika * self.vauhti
        return

xyz = 0
while xyz < 10000:
    for i in range(1, 11):
        x = random.randint(100, 200)
        globals()[f"Auto{i}"] = Auto(f"ABC-{i}", x)

    for i in range(1, 11):
        x = random.randint(-10, 15)

        globals()[f"Auto{i}"].kiihdyta(x)

        print(globals()[f"Auto{i}"].vauhti)

    print("")

    for i in range(1, 11):
        globals()[f"Auto{i}"].kulje(1)

        print(globals()[f"Auto{i}"].matka)

    for i in range(1, 11):
        ls = []
        ls.append(globals()[f"Auto{i}"].matka)
        if 10000 in ls:
            xyz = 10000
    