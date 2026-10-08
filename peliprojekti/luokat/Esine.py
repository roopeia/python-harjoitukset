class Esine:
    esineet = []
    def  __init__(self, id, nimi):
        self.id = id
        self.nimi = nimi
        Esine.esineet.append(self)

class Avain(Esine):
    def __init__(self, id, nimi):
        super().__init__(id, nimi)
        #Ajattelin laittaa avaimelle extra muuttujia sen takia tein siitä oman luokan
        
class Varuste(Esine):
    def __init__(self, id, nimi, hp, dmg):
        super().__init__(id, nimi)
        self.hp = hp
        self.dmg = dmg