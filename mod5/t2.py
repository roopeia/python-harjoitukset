#oita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuuma?"))

while tuuma >= 0:
    print(tuuma * 2.54)
    tuuma = float(input("Anna tuuma?"))
print("Negatiivinen tuumamäärä")


