class Square:

    def __init__(self, side=0):
        print("I am constructor")
        self._x = side

    @property  # dekoruemy funkcję x - domyślnie jako get
    def x(self):
        return self._x

    @x.setter  # powyższą funkcję x wykorzystujemy, by dekorować funkcję poznajdującą się poniżej(xd została zapisana, by odróżnić ją od gettera)
    def xd(self, Newside):
        self._x = Newside

    def Area(self):
      '''
      This is my docString!
      '''
      return self._x ** 2


square1 = Square(4)
print(square1.x)
square1.xd = 5
print(square1.x)
print("Dokumentacja funkcji")
print(square1.Area.__doc__)