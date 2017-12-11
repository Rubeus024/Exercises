

from Vector import Wektor

V1=Wektor(5,12)

if (__name__=="__main__"):
    print("Współrzędne Wektora V1")
    print(str(__name__),"666")
    print("")
    print(V1.Description())

    print(V1.xCoord)
    V1.xCoord=-120
    print(V1.xCoord)