import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, "save.json")
path2 = os.path.join(dir, "intro.txt")
class pelaaja:
    def __init__(self, nimi, taso, varusteet):
        self.nimi = nimi
        self.taso = taso
        self.varusteet = varusteet
        self.tallennus_data = {
            "nimi": self.nimi,
            "taso": self.taso,
            "varusteet": self.varusteet
        }

    def tallenna(self):
        self.tallennus_data["nimi"] = self.nimi
        self.tallennus_data["taso"] = self.taso
        with open(path, "w") as tiedosto:
            json.dump(self.tallennus_data, tiedosto)




Pelaaja1 = 0

with open(path2, "r") as tiedosto:
    teksti = tiedosto.read()
    print(teksti)

with open(path, "r") as tiedosto:
    first_char = tiedosto.read(1)
    if not first_char:
        nimi = input("nimi: ")
        Pelaaja1 = pelaaja(nimi, 0, [])
    else:
        with open(path, "r") as tiedosto:
            data = json.load(tiedosto)
            Pelaaja1 = pelaaja(data["nimi"], data["taso"], data["varusteet"])

print(Pelaaja1.nimi)

Pelaaja1.nimi = input("nimi>")
Pelaaja1.taso = int(input("taso>"))
Pelaaja1.varusteet.append(input("varuste>"))

print(Pelaaja1.taso)

print(Pelaaja1.tallennus_data)

Pelaaja1.tallenna()
print(Pelaaja1.tallennus_data)
"""
with open(path, "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)
with open(path, "r") as tiedosto:
    data_luettu = json.load(tiedosto)
"""