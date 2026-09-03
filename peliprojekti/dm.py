nimi = input("mikä on nimesi?")
ika = int(input("kuinka vanha olet?"))

print(nimi, ika)

if ika <= 12:
    print("olet alaikäinen")
    quit()
else:
    print("hei", nimi)

komento = ""

while komento != "lopeta":
    komento = input("Anna komento: ls_ika, ls_nimi, ls_profiili, lopeta ")
    if komento == "ls_ika":
        print(ika)
    elif komento == "ls_nimi":
        print(nimi)
    elif komento == "ls_profiili":
        print(ika, nimi)