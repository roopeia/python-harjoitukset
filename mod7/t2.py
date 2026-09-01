#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def noppa(luku):
    luku = random.randint(1, luku)
    return luku

tahko = int(input("kuinka monta tahkoa? "))

while True:
    heitto = input("Heitä noppaa (Enter) ")
    if heitto: True
    num = noppa(tahko)
    print(num)
    if num == tahko:
        break
