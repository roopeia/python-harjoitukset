DUNGEONMASTER

Roope Aaltonen

```text
Ohjelman-rakenne/
|
├──main.py
└──luokat/
    ├──__init__.py
    ├──hahmot.py
    ├──esine.py
    └──huone.py
└──funktio/
    ├──__init__.py
    └──valikko.py
```
Tässä pelissa on tarkoitus kulkea huoneiston läpi ja kerätä varusteita,
joita käytetään viimeisen huoneen pahista vastaan.

Varusteissa on arvot hp ja dmg. arvot lisätään pelaajan hp ja dmg arvoihin.

viimeisen huoneen pahiksella on itselläkin hp ja dmg arvot jotka ovat staattiset.

pelaajalla on mahdollisuus lyödä pahista jolloin pahiksen hp:sta miinustetaan pelaajan dmg arvo.
Aina, kun pelaaja lyö pahista, pahis lyö pelaajaa, jolloin pelaajan hp:sta miinustetaan pahiksen dmg arvo.

peli päätty kun joko pahiksen tai pelaajan hp tippuu nollaan.

jos pelaajaan keräämistä esineistä saatu hp ja dmg on tarpeeksi korkea, 
niin pahiksen hp tippuu nollaan ennen pelaajaa ja pelaaja voittaa


Kestävä kehitys juttu on kyssäri kierrätyksestä -_-(tein pelin ennen kuin näin vaatimukset)