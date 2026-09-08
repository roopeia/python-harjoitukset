#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

ls =  [1, 2, 3, 4, 5]

def summa(obj):
    sum = 0
    for i in obj:
        sum = sum + i
    return sum

tulos = summa(ls)
print(tulos)
