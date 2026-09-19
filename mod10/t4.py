
import random

class Auto:

    def __init__(self, rek, hn):
        self.rek = rek
        self.hn = hn
        self.vauhti = 0
        self.matka = 0

    def kiihdyta(self, kmh):
        if kmh + self.vauhti <= self.hn and kmh + self.vauhti >= 0:
            self.vauhti = self.vauhti + kmh
        elif self.vauhti + kmh >= self.hn:
            self.vauhti = self.hn
        return

    def ebrake(self):
        self.vauhti = self.vauhti - 200
        if self.vauhti < 0:
            self.vauhti = 0
        return

    def kulje(self, aika):
        self.matka = self.matka + aika * self.vauhti
        return

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            x = random.randint(-10, 15)
            auto.kiihdyta(x)
        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("")
        print(f"{'Rek':<10}{'Huippu':<10}{'Nopeus':<10}{'Matka':<10}")

        for auto in self.autot:
            print(f"{auto.rek:<10}{auto.hn:<10}{auto.vauhti:<10}{auto.matka:<10}")

    def kilpailu_ohi(self):
        if max(auto.matka for auto in self.autot) >= 8000:
            return True
        else:
            return False


autot = []

for i in range(1, 11):
    x = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i}", x))

Kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot)

Laskuri = 0

while Kilpailu1.kilpailu_ohi() == False:
    
    Kilpailu1.tunti_kuluu()

    Kilpailu1.kilpailu_ohi()

    Laskuri = Laskuri + 1
    if Laskuri == 10:
        Kilpailu1.tulosta_tilanne()
        Laskuri = 0

Kilpailu1.tulosta_tilanne()


