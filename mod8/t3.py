#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, 
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, 
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä 
# vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, 
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. 
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. 
# Löydät koodeja helposti selaimen avulla.)

lentokentät = {"EFHK": "Helsinki-Vantaa"}

while True:
    print("")
    print("(1): Hae asemaa ICAO koodilla")
    print("(2): Syötä uusi asema")
    print("(3): lopeta")
    x = int(input(">"))
    if x == 1:
        icao = input("Anna ICAO koodi>")
        print(lentokentät[icao])
    elif x == 2:
        icao = input("Anna ICAO koodi>")
        nimi = input("Anna nimi>")
        lentokentät[icao] = nimi
    elif x == 3:
        quit()