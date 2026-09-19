#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
#Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, 
#joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
        self.ak = yk
        self.yk = ak
        self.hissit = hissit
        self.Hissit = []
        for i in range(0, hissit):
            self.Hissit.append(Hissi(f"hissi{i + 1}", yk, ak))

    def aja_hissiä(self, no, kohde):
        no = no - 1
        self.Hissit[no].siirry_kerrokseen(kohde)
    
    
talo1 = Talo(5, 1, 2)

talo1.aja_hissiä(1, 4)
talo1.aja_hissiä(2, 5)
talo1.aja_hissiä(1, 2)


