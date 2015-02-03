#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Un felicitador pel cunyao :3

from datetime import date

class FelicitadorCunyao():
    CUNYAO_BORN = date(1995, 2, 3)

    def __init__(self):
        if self.cumpleCunyao():
            self.felicitarCunyao()
        else:
            self.pene()

    def cumpleCunyao(self):
        return (date.today().day == self.CUNYAO_BORN.day and
                date.today().month == self.CUNYAO_BORN.month)

    def felicitarCunyao(self):
        print "FELIÇOS " + self.edatCunyao() + " CUNYAO!!! :D"
        return

    def edatCunyao(self):
        return str(date.today().year - self.CUNYAO_BORN.year)

    def pene(self):
        print "pene, avui no es :("
        return

if __name__ == "__main__":
    lol = FelicitadorCunyao()
    exit(0)

            
