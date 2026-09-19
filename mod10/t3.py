#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. 
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, nimi, yk, ak):
        self.nimi = nimi
        self.yk = yk
        self.ak = ak
        self.kerros = 0

    def siirry_kerrokseen(self, x):
        if self.kerros > x:
            while self.kerros != x:
                self.kerros_alas()
        if self.kerros < x:
            while self.kerros != x:
                self.kerros_ylös()
        print(f"{self.nimi} kerrokesessa {self.kerros}")
        
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        if self.kerros >= self.yk:
            self.kerros = self.yk

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        if self.kerros <= self.ak:
            self.kerros = self.ak

class Talo:
    def __init__(self, yk, ak, hissit):
        self.ak = ak
        self.yk = yk
        self.hissit = hissit
        self.Hissit = []
        for i in range(0, hissit):
            self.Hissit.append(Hissi(f"hissi{i + 1}", yk, ak))

    def aja_hissiä(self, no, kohde):
        no = no - 1
        self.Hissit[no].siirry_kerrokseen(kohde)

    def palohälytys(self):
        for hissi in self.Hissit:
            hissi.siirry_kerrokseen(self.ak)

    
    
talo1 = Talo(5, 1, 2)

talo1.aja_hissiä(1, 4)
talo1.aja_hissiä(2, 5)
talo1.aja_hissiä(1, 2)

talo1.palohälytys()