from luokat import Hahmot, Huone, Esine
from funkkarit import paavalikko

import json
import os

from luokat import Avain, Bosshuone, Lukittu, Varuste

dir = os.path.dirname(os.path.abspath(__file__))
save = os.path.join(dir, "save.json")
intro1 = os.path.join(dir, "intro.txt")

"""
ika = int(input("kuinka vanha olet?"))

if ika <= 12:
    print("olet alaikäinen")
    quit()
else:
    print("hei", nimi)
"""

miekka = Varuste(0, "Miekka", 0, 25)
kilpi = Varuste(1, "Kilpi", 50, 25)
haarniska = Varuste(2, "Haarniska", 50, 0)
avain = Avain(3, "Avain")
kivi = Esine(4, "kivi")
vihu = Hahmot.NPC("Vihu", 100, 50)
Huone1 = Huone("huone1", miekka, "eka")
Huone2 = Huone("huone2", kilpi, "toka")
Huone3 = Huone("huone3", haarniska, "kolmas")
Huone4 = Huone("huone4", avain, "neljäs")
Huone5 = Bosshuone("huone5", kivi, "viides", avain, vihu)

komento = 0
Pelaaja1 = 0

with open(save, "r") as tiedosto:
    first_char = tiedosto.read(1)
    if not first_char:
        nimi = input("nimi: ")
        Pelaaja1 = Hahmot.Pelaaja(nimi, 0, [])

        with open(intro1, "r") as tiedosto:
            teksti = tiedosto.read()
            print(teksti)
    else:
        with open(save, "r") as tiedosto:
            data = json.load(tiedosto)
            Pelaaja1 = Hahmot.Pelaaja(data["nimi"], data["huone"], data["esineetid"])

paavalikko(Pelaaja1, save)

while Pelaaja1.hp != 0:
    print("")
    print("(1)lyö")
    print("(2)Liiku seuraavaan huoneeseen")
    print("(3)Liiku edelliseen huoneeseen")
    print("(4)kerää huoneesta esine")
    print("(5)valikko")
    komento = int(input(">"))
    if komento == 1:
        Pelaaja1.attack()
        if Pelaaja1.huone == vihu.huone:
            vihu.attack()
        if vihu.hp == 0:
            break
        
    elif komento == 2:
        Pelaaja1.liiku_eteen()
    elif komento == 3:
        Pelaaja1.liiku_taakse()
    elif komento == 4:
        Pelaaja1.keraa_esine()
    elif komento == 5:
        paavalikko(Pelaaja1, save)


if Pelaaja1.hp == 0:
    print("kuolit")
if vihu.hp == 0:
    print("voitit")