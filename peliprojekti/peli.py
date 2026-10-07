from luokat import Hahmot, Huone, Esine
from funkkarit import paavalikko, profiili, init

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
sinko = Varuste(4, "Sinko", 0, 1000)
vihu = Hahmot.NPC("Gul'dan", 100, 50)
Huone1 = Huone("huone1", miekka, "Astuit ensimmäiseen huoneeseen. huoneesta löytyy miekka")
Huone2 = Huone("huone2", kilpi, "Etenit toiseen huoneeseen. Näet lattialla kilven")
Huone3 = Huone("huone3", haarniska, "Kuljit saliin jossa on koristeena haarniskoja")
Huone4 = Huone("huone4", avain, "Etenit neljänteen huoneeseen. huoneen lattialla kimmeltää")
Huone5 = Bosshuone("huone5", sinko, "Astut suureen saliin jossa näät pahamaineisen velho guldanin", avain, vihu)

komento = 0

with open(intro1, "r") as tiedosto:
    teksti = tiedosto.read()
    print(teksti)

Pelaaja1 = init(save)

paavalikko(Pelaaja1, save)

while Pelaaja1.hp != 0:
    print("")
    if sinko in Pelaaja1.esineet:
        print("(0)Laukaise Armor-Piercing infantry light arm system(APILAS)")
    print("(1)lyö")
    print("(2)Liiku seuraavaan huoneeseen")
    print("(3)Liiku edelliseen huoneeseen")
    print("(4)kerää huoneesta esine")
    print("(5)valikko")
    komento = int(input(">"))
    if komento == 1 or komento == 0:
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