#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def noppa(luku):
    luku = random.randint(1, 6)
    return luku

num = 0

while True:
    heitto = input("Heitä noppaa (Enter) ")
    if heitto: True
    num = noppa(num)
    print(num)
    if num == 6:
        break