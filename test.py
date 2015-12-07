__author__ = 'root'

class Shape:
    def __init__(self, r):
        assert r>0, "That ain't gonna work!"
        self.__r = r

    @property
    def radius(self):
        return self.__r;

    @radius.setter
    def radius(self, r):
        self.__r = r

shape = Shape(-5)
print(shape.radius)
shape.radius = 10
print(shape.radius)
