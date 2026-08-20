#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).

user = input("Käyttäjä:")
pword = input("Salasana:")
kerrat = 1

realuser = "user"
realpword = "pword"

while kerrat != 5:
    user = input("Käyttäjä:")
    pword = input("Salasana:")
    kerrat = kerrat + 1
    if user == realuser and pword == realpword:
        print("Tervetuloa")
        break

if kerrat == 5:
    print("pääsy evätty")
