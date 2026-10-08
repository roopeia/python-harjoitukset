from .Huone import Huone, Lukittu, Bosshuone
from .Esine import Esine, Avain, Varuste
import os
import json

class Pelaaja:
    pelaajat = []
    def __init__(self, nimi, huone, esineetid):
        self.nimi = nimi
        self.hp = 1
        self.dmg = 0
        self.huone = huone
        self.esineet = []
        #olioita ei voi tallentaa json tiedostoon joten tallennan olioon liitetyn numeron
        self.esineetid = esineetid
        for id in esineetid:
            self.esineet.append(Esine.esineet[id])
        """
        for esine in self.esineet:
            if hasattr(esine, "hp"):
                self.hp += esine.hp
            elif hasattr(esine, "dmg"):
                self.dmg += esine.dmg
        """
        self.tallennus_data = {
            "nimi": self.nimi,
            "huone": self.huone,
            "esineetid": self.esineetid
        }
        Pelaaja.pelaajat.append(self)

    def liiku_eteen(self):

        if self.huone >= len(Huone.huoneet) - 1:
            print("Et voi mennä eteenpäin.")
            return

        seuraava = Huone.huoneet[self.huone + 1]

        if isinstance(seuraava, Bosshuone):
            if seuraava.vaatimus in self.esineet:
                self.huone += 1
                print("ovi aukaistu")
                print(Huone.huoneet[self.huone].desc)
                print(f"{seuraava.npc.nimi}, hp: {seuraava.npc.hp}")
            else:
                print("ovi lukossa")
        elif isinstance(seuraava, Lukittu):
            if seuraava.vaatimus in self.esineet:
                self.huone += 1
                print("ovi aukaistu")
                print(Huone.huoneet[self.huone].desc)
            else:
                print("ovi lukossa")
        else:
            self.huone += 1
            print(Huone.huoneet[self.huone].desc)
        
    

    def attack(self):
        huone = Huone.huoneet[self.huone]
        if hasattr(huone, "npc"):
            if huone.npc.hp != 0:
                huone.npc.hp -= self.dmg
                if huone.npc.hp < 0:
                    huone.npc.hp = 0
                print(f"Vihollisen hp: {huone.npc.hp}")
                print(f"oma hp: {self.hp}")
            else: 
                print("Kuoli jo!")
        


    def liiku_taakse(self):

        if self.huone <= 0:
            self.huone == 0
            print("olet ensimmäisessä huoneessa")
            return
        else:
            self.huone -= 1
            print(Huone.huoneet[self.huone].nimi)

    def keraa_esine(self):
        huone = Huone.huoneet[self.huone]
        
        if huone.esine not in self.esineet:
            self.esineet.append(huone.esine)
            self.esineetid.append(huone.esine.id)
            if hasattr(huone.esine, "hp"):
                self.hp += huone.esine.hp
            if hasattr(huone.esine, "dmg"):
                self.dmg += huone.esine.dmg
            print(f"keräsit esineen: {huone.esine.nimi}")


    def tallenna(self, path):
        self.tallennus_data["nimi"] = self.nimi
        self.tallennus_data["huone"] = self.huone
        with open(path, "w") as tiedosto:
            json.dump(self.tallennus_data, tiedosto)

class NPC:
    def __init__(self, nimi, hp, dmg):
        self.huone = 4
        self.nimi = nimi
        self.hp = hp
        self.dmg = dmg

    def attack(self):
        pelaaja = Pelaaja.pelaajat[0]
        if pelaaja.hp != 0 and self.hp != 0:
            pelaaja.hp -= self.dmg
            if pelaaja.hp < 0:
                pelaaja.hp = 0