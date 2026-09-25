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

class SAuto(Auto):
    def __init__(self, rek, hn, kwh):
        super().__init__(rek, hn)
        self.kwh = kwh

class PAuto(Auto):
    def __init__(self, rek, hn, litrat):
        super().__init__(rek, hn)
        self.litrat = litrat

sähköauto = SAuto("ABC-15", 180, 52.5)
polttomoottoriauto = PAuto("ACD-123", 165, 32.3)
sähköauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(150)

sähköauto.kulje(3)
print(f"{sähköauto.rek}: {sähköauto.matka}km")

polttomoottoriauto.kulje(3)
print(f"{polttomoottoriauto.rek}: {polttomoottoriauto.matka}km")