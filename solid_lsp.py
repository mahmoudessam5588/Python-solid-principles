"""Lescott substitution principle:if you have an interface abd base class you can stick a derived class from there and everything would work"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width*self._height

    def __str__(self):
        return f'Width : {self._width}, height : {self._height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self,size):
        Rectangle.__init__(self,size,size)
    @Rectangle.width.setter
    def width(self,value):
        self._width = self._height = value
    @Rectangle.height.setter
    def height(self,value):
        self._width = self._height = value         
            
        


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'I expected area of {expected} ,got {rc.area}')
