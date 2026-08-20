#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

numero = 1
while numero < 1000:
    if numero % 3 == 0:
        print(numero)
    numero = numero + 1
    