#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#  Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
#Esimerkki ohjelman toiminnasta:

#leiviska = leiviska * 20 * 32



leiviska = float(input("anna leiviskat"))
leiviskag = (leiviska * 20 * 32 * 13.3)

naulat = float(input("anna naulat"))
naulatg = (naulat * 32 * 13.3)

luodit = float(input("anna luodit"))
luoditg = (luodit * 13.3)

kokosumma = leiviskag + naulatg + luodit
kilot = int(kokosumma / 1000) * 1000


print(f"{int(kokosumma / 1000)}kiloa ja {int(kokosumma - kilot)} grammaa")


