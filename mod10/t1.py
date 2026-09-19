#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. 
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), 
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, yk, ak):
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
        print(self.kerros)  
        

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        if self.kerros >= self.yk:
            self.kerros = self.yk

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        if self.kerros <= self.ak:
            self.kerros = self.ak

h1 = Hissi(10, 1)

h1.siirry_kerrokseen(6)
h1.siirry_kerrokseen(1)
