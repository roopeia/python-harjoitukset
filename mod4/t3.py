#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sex = input("Mikä on sukupuolesi? (M/N)")
hemo = int(input("Mikä on hemoglobiini arvosi?"))

if sex == "M" and hemo < 134:
    print("hemoglobiiniarvosi on alhainen")
elif sex == "M" and hemo > 195:
    print("Hemoglobiiniarvo on korkea")
elif sex == "M":
    print("Hemoglobiini on normaali")


if sex == "N" and hemo < 117:
    print("hemoglobiiniarvosi on alhainen")
elif sex == "N" and hemo > 175:
    print("Hemoglobiiniarvo on korkea")
elif sex == "N":
    print("Hemoglobiinisi on normaali")