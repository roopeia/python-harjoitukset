
import random

class Auto:

    def __init__(self, rek, hn):
        self.rek = rek
        self.hn = hn
        self.vauhti = 0
        self.matka = 0

Auto1 = Auto("ABC-123", 142)
print(f"rek: {Auto1.rek:<10}huippu: {Auto1.hn:<10}vauhti: {Auto1.vauhti:<10}matka: {Auto1.matka:<10}")