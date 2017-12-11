from math import sqrt


class Wektor:

    def __init__(self,x,y):
        self._xCoord=x # prywatna zmienna _ (jest to umoan zasada)
        self._yCoord=y
    @property
    def xCoord(self):
        return self._xCoord
    @xCoord.setter
    def xCoord(self,x1):
        if(x1<-100):
            print("Za duża ujemna liczba")

        self._xCoord=x1



    def Module(self):
        return sqrt((self.xCoord ** 2 + (self.yCoord) ** 2))

    def Description(self):
        print("Ta klasa tworzy dwuwymiarowy wrktor rzędu 1. Nazwa klasy to: {}".format(__name__))

