#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#  Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

luku = input("luku")


while luku != "":
    luvut.append(luku)
    luku = input("luku")

isoin = max(luvut)
pienin = min(luvut)

print(f"isoin: {isoin}, pienin: {pienin}")

