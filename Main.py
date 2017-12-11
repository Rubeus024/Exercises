

from Vector import Wektor

V1=Wektor(5,12)

if (__name__=="__main__"):
    #atrybut __name__ wskazuje, czy moduł jest importowany, czy nie
    print("Współrzędne Wektora V1")
    print(str(__name__),"666")
    print("")
    print(V1.Description())

    # Zabawa z koordynatami
    print(V1.xCoord)
    V1.xCoord=-120
    print(V1.xCoord)
    print("Pseudo prywatna zmienna: {} ".format(V1._xCoord))