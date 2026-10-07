from luokat.Hahmot import Pelaaja
import json 

def init(save):
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
            with open(save, "w") as tiedosto:
                json.dump(tallennus_data, tiedosto)
            with open(save, "r") as tiedosto:
                data = json.load(tiedosto)
                Pelaaja1 = Pelaaja(data["nimi"], data["huone"], data["esineetid"])
        else:
            with open(save, "r") as tiedosto:
                data = json.load(tiedosto)
                Pelaaja1 = Pelaaja(data["nimi"], data["huone"], data["esineetid"])
    return Pelaaja1