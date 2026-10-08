from luokat.Hahmot import Pelaaja
import json 

def init(save):
    #funktio luo pelaaja objektin ja tallentaa tyhjän tietosanakirjan json tiedostoon
    #jos save tiedostosta löytyy jo tallennus se lataa sen tiedot
    with open(save, "r") as tiedosto:
        first_char = tiedosto.read(1)
        if not first_char:
            nimi = input("nimi: ")
            Pelaaja1 = Pelaaja(nimi, 0, [])
            tallennus_data = {
                "nimi": nimi,
                "huone": 0,
                "esineetid": []
            }
            # uudelleen kirjoittaa tiedoston aloitus arvoihin
            with open(save, "w") as tiedosto:
                json.dump(tallennus_data, tiedosto)
            # tällä muutetaan pelaaja olion arvot vielä alku pisteeseen
            with open(save, "r") as tiedosto:
                data = json.load(tiedosto)
                Pelaaja1 = Pelaaja(data["nimi"], data["huone"], data["esineetid"])
        else:
            with open(save, "r") as tiedosto:
                data = json.load(tiedosto)
                Pelaaja1 = Pelaaja(data["nimi"], data["huone"], data["esineetid"])
    return Pelaaja1