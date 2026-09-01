# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
# Käytä for-toistorakennetta.

import random

arpakuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for i in range(arpakuutiot):
    luku = random.randint(1,6)
    summa = summa + luku

print(summa)
