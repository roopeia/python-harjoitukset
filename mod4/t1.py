# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kala = int(input("kuinka pitkä kuha sentteinä?"))
if kala < 37:
    print("kuha on alimittainen, siitä puuttuu", 37 - kala, "cm")