#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#Vihje: tutustu random.randint()-funktion käyttöön.

import random

trilock = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
print(trilock)
quadlock = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print(quadlock)