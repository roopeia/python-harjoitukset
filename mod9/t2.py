
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

Auto1 = Auto("ABC-1", 142)

Auto1.kiihdyta(30)
Auto1.kiihdyta(70)
Auto1.kiihdyta(50)
print(Auto1.vauhti)
Auto1.ebrake()
print(Auto1.vauhti)