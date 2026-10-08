class Huone:
    huoneet = []
    def __init__(self, nimi, esine, desc):
        self.nimi = nimi
        self.esine = esine
        self.desc = desc
        Huone.huoneet.append(self)


class Lukittu(Huone):
    def __init__(self, nimi, esine, desc, vaatimus):
        super().__init__(nimi, esine, desc)
        self.vaatimus = vaatimus


class Bosshuone(Lukittu):
    def __init__(self, nimi, esine, desc, vaatimus, npc):
        super().__init__(nimi, esine, desc, vaatimus)
        self.npc = npc
        
