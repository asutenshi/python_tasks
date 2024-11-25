from abc import abstractmethod, ABC
from math import pi

class Shape3d(ABC):
    def __init__(self):
        self._surface_area = 0
        self._volume = 0
    
    @abstractmethod
    def get_surface_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Ellipsoid(Shape3d):
    def __init__(self, a, b, c):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            if a >= 0 and b >= 0 and c >= 0:
                self._a = a
                self._b = b
                self._c = c
            else: raise ValueError('Радиусы не могут быть отрицательным числом')
        else: return NotImplemented

    def get_surface_area(self):
        p = 1.6075
        return 4 * pi * ((self._a**p * self._b**p + self._a**p * self._c**p + self._b**p * self._c**p) / 3)**(1/p)

    def get_volume(self):
        return 4 / 3 * pi * self._a * self._b * self._c

    def __str__(self):
        return f'Ellipsoid(a={self._a}, b={self._b}, c={self._c})'

class Cphere(Ellipsoid):
    def __init__(self, r):
        Ellipsoid.__init__(self, r, r, r)
    def __str__(self):
        return f'Cphete(r={self._a})'

class Parallelepiped(Shape3d):
    def __init__(self, a, b, c):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            if a >= 0 and b >= 0 and c >= 0:
                self._a = a
                self._b = b
                self._c = c
            else: raise ValueError('Стороны не могут быть отрицательным числом')
        else: return NotImplemented
    
    def get_surface_area(self):
        return 2 * (self._a * self._b + self._b * self._c + self._a * self._c)

    def get_volume(self):
        return self._a * self._b * self._c

    def __str__(self):
        return f'Parallelepiped(a={self._a}, b={self._b}, c={self._c})'


class Cube(Parallelepiped):
    def __init__(self, a):
        Parallelepiped.__init__(self, a, a, a)

    def __str__(self):
        return f'Cube(a={self._a})'

class Cylinder(Shape3d):
    def __init__(self, r, h):
        if isinstance(r, (int, float)) and isinstance(h, (int, float)):
            if r >= 0 and h >= 0:
                self._r = r
                self._h = h
            else: raise ValueError('Радиус или высота не могут быть отрицательным числом')
        else: return NotImplemented

    def get_surface_area(self):
        return 2 * pi * self._r * self._h + 2 * (pi * self._r**2)

    def get_volume(self):
        return pi * self._r**2 * self._h

    def __str__(self):
        return f'Cylinder(r={self._r}, h={self._h})'

e = Ellipsoid(3, 4, 5)
print(e.get_volume(), e.get_surface_area())
cph = Cphere(4)
print(cph.get_volume(), cph.get_surface_area())
p = Parallelepiped(100, 100, 100)
print(p.get_volume(), p.get_surface_area())
cube = Cube(100)
print(cube.get_volume(), cube.get_surface_area())
cil = Cylinder(4, 5)
print(cil.get_volume(), cil.get_surface_area())

def volume_checker(*args):
    figures = args
    volumes = []
    for figure in figures: volumes.append(figure.get_volume())
    for i, volume in enumerate(volumes): 
        if volume >= sum([x for x in volumes if x != volume]): print(figures[i])
volume_checker(e, cph, p, cube, cil)
