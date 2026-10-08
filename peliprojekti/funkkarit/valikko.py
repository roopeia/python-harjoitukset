from luokat.Hahmot import Pelaaja
from .init import init


def profiili(pelaaja, path):
    pelaaja = pelaaja
    path = path
    print("")
    print(pelaaja.nimi)
    print(f"huone: {pelaaja.huone}")
    print("--Esineet--")
    for esine in pelaaja.esineet:
        print(esine.nimi)
    print("(1)Muokkaa profiilia")
    print("(2)Takaisin")
    komento = input(">")
    if komento == "1":
        uusinimi = input("Uusi nimi: ")
        pelaaja.nimi = uusinimi
        pelaaja.tallenna(path)
    elif komento == "2":
        return


def paavalikko(pelaaja, path):
    pelaaja = pelaaja
    path = path
    komento = ""
    while komento != "1":
        print("")
        print("(1)pelaa")
        print("(2)tallenna tiedostoon")
        print("(3)tyhjennä tallennus")
        print("(4)profiili")
        print("(5)lopeta")
        komento = input(">")
        if komento == "2":
            pelaaja.tallenna(path)
        elif komento == "3":
            open(path, 'w').close()
            if input("tee uusi profiili y/n") == "y":
                init(path)
        elif komento == "4":
            profiili(pelaaja, path)
        elif komento == "5":
            quit()
    return

