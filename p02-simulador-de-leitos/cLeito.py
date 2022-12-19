#!/usr/bin/env python3

import random

cor_reset = "\033[00m"
cor_neonatal = "\033[92m"
cor_pediatrico = "\033[96m"
cor_adulto = "\033[95m"

# utilizado para geração do nome
alfa = ("A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z")
##

class Leito:
    def __init__(self, f_etaria):
        self.f_etaria = f_etaria
        self.hospital = ""
        for i in range(3):
            self.hospital += random.choice(alfa)

    def __str__(self):
        out = self.hospital + '-'
        if self.f_etaria == 'a':
            out =  f"%s{out + str(id(self))}"% cor_adulto
        elif self.f_etaria == 'p':
            out = f"%s{out + str(id(self))}"%cor_pediatrico
        elif self.f_etaria == 'n':
            out = f"%s{out + str(id(self))}"%cor_neonatal

        return out + cor_reset

if __name__ == "__main__":
    ln = Leito('n')
    lp = Leito('p')
    la = Leito('a')
    print(ln, lp, la)
