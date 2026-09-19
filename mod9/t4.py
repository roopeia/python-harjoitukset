
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

autot = []

for i in range(1, 11):
    x = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i}", x))


while max(auto.matka for auto in autot) < 10000:
    
    for auto in autot:
        x = random.randint(-10, 15)
        auto.kiihdyta(x)

    print("")

    for auto in autot:
        auto.kulje(1)

print(f"{'Rek':<10}{'Huippu':<10}{'Matka':<10}")

for auto in autot:
    print(f"{auto.rek:<10}{auto.hn:<10}{auto.matka:<10}")