#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, 
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

def pizza(d, euro):
    r = (d / 100)/ 2
    a = 3.141 * r**2
    suhde = euro / a
    return suhde


d = float(input("ekan pizzan halkaisija (cm)"))
e = float(input("ekan pizzan hinta"))


d2 = float(input("tokan pizzan halkaisija (cm)"))
e2 = float(input("tokan pizzan hinta"))

p = pizza(d, e)
p2 = pizza(d2, e2)

if p < p2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif p2 < p:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("pizzat yhtä edullisia")