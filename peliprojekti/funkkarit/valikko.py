from luokat.Hahmot import Pelaaja


def paavalikko(pelaaja, path):
    pelaaja = pelaaja
    path = path
    komento = 0
    while komento != 1:
        print("")
        print("(1)pelaa")
        print("(2)tallenna tiedostoon")
        print("(3)profiili")
        print("(4)lopeta")
        komento = int(input(">"))
        if komento == 2:
            pelaaja.tallenna(path)
        elif komento == 3:
            print(pelaaja.nimi)
        elif komento == 4:
            quit()
    return


"""
def profiili(pelaaja, path):
    komento = 0
    pelaaja = pelaaja
    path = path
    while komento != 2:
        print("")
        print("PROFIILI")
        print(pelaaja.nimi)
        print("(1)muokkaa")
        print("(2)takaisin")
        print("(3)tallenna tiedostoon")
        komento = int(input(">"))
        if komento == 1:
            pelaaja.nimi = input("aseta nimi: ")
        elif komento == 3:
            pelaaja.tallenna(path)

    return pelaaja.nimi
"""
