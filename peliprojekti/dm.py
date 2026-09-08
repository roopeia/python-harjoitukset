
lista = []
komento = ""

nimi = input("mikä on nimesi?")
ika = int(input("kuinka vanha olet?"))

print(nimi, ika)

if ika <= 12:
    print("olet alaikäinen")
    quit()
else:
    print("hei", nimi)

def ls_add():
    x = input("Listaa asia: ")
    lista.append(x)
    print("asia listattu")
    return

def ls(obj):
    if not obj:
        print("Lista on tyhjä")
    for i in obj:
        print(i)
    return

def profiili(x, y):
    komento = ""
    nimi = x
    ika = y
    while komento != "takaisin":
        print("")
        print("PROFIILI")
        print(nimi, ika)
        komento = input("Anna komento: muokkaa, takaisin: ")
        if komento == "muokkaa":
            nimi = input("aseta nimi: ")
            ika = int(input("aseta ikä: "))
    return nimi, ika


while komento != "lopeta":
    komento = input("minkä toiminnon haluat suorittaa: ls, ls_add, profiili, lopeta: ")
    if komento == "ls":
        ls(lista)
    elif komento == "ls_add":
        ls_add()
    elif komento == "profiili":
        nimi, ika = profiili(nimi, ika)
