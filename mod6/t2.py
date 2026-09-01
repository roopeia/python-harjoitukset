#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
# Vihje: 
# listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []

luku = input("luku ")

try:
    luku = int(luku)
    luvut.append(luku)
except:
    print("huono")

while luku != "":
    luku = input("luku ")
    try:
        luku1 = int(luku)
        luvut.append(luku1)
    except:
        print("")

top5 = sorted(luvut, reverse=True)[:5]
print(top5)
        