#!/usr/bin/env python
# -*- coding: utf-8 -*-
from static import wagi, slownik_znakow, sad


class NumerKW:
    def __init__(self, nr):
        self.nr = nr
        self.kod_sad, self.numer = self.nr.split('/')

    def uzupelnij_numer(self):
        zera = 8 - len(self.numer)
        return self.kod_sad + zera * '0' + self.numer

    def cyfra_kontrolna(self):
        numer = self.uzupelnij_numer()
        if len(numer) != 12:
            raise KeyError
        suma = 0
        for nr, z in enumerate(numer[:12]):
            suma += slownik_znakow[z.upper()] * wagi[nr]
        cyfra = suma % 10

        numer_kw = '/'.join((numer[0:4].upper(), numer[4:12], str(cyfra)))
        return numer_kw


class NumeryKW:
    def __init__(self, filename):
        self.filename = filename
        self.kod_sad = filename.split('.')[0]

    def uzupelnij_numer(self, numer):
        zera = 8 - len(numer)
        return self.kod_sad + zera * '0' + numer

    def cyfra_kontrolna(self, numer):
        suma = 0
        for nr, z in enumerate(numer[:12]):
            suma += slownik_znakow[z.upper()] * wagi[nr]
        cyfra = suma % 10

        numer_kw = '/'.join((numer[0:4].upper(), numer[4:12], str(cyfra)))
        return numer_kw

    def oblicz_numery(self):
        with open(self.filename, 'r') as p:
            dane = [i.strip() for i in p.readlines()]
            for nr, kw in enumerate(dane):
                nr_kw = self.uzupelnij_numer(kw)
                if len(nr_kw) == 12:
                    dane[nr] = self.cyfra_kontrolna(nr_kw)
        p.close()
        with open(self.filename, 'w') as w:
            for i in dane:
                w.writelines(i+'\n')
        w.close()


if __name__ == "__main__":
    pass