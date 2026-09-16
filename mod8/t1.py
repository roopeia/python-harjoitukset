#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, 
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina 
# monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# Kysytään kuukauden numero
kuukausi = int(input("Anna kuukauden numero: "))

indeksi = (kuukausi % 12)//3
print(vuodenajat[indeksi])