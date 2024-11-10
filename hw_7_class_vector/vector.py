import math

class Vector2D():
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        if isinstance(x1, int) and isinstance(x2, int) and isinstance(y1, int) and isinstance(y2, int):
            self.__x1 = x1
            self.__y1 = y1
            self.__x2 = x2
            self.__y2 = y2
            self.dx = self.__x2 - self.__x1
            self.dy = self.__y2 - self.__y1
        else: return NotImplemented

    def length(self):
        return round(math.sqrt((self.dx)**2 + (self.dy)**2), 3)

    def angle(self):
        return round(math.atan2((self.dy), (self.dx)) * 180 / math.pi)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x1, self.__y1, (self.dx + other.dx + self.__x1), (self.dy + other.dy + self.__y1))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x1, self.__y1, (self.dx - other.dx + self.__x1), (self.dy - other.dy + self.__y1))
        else: return NotImplemented

    def scalar_mul(self, other):
        if isinstance(other, Vector2D):
            return (self.dx) * (other.dx) + (self.dy) * (other.dy)
        else: return NotImplemented

    def __str__(self):
        return f'{self.__x1, self.__y1}{self.__x2, self.__y2}'

v = Vector2D(1, 2, 3, 4)
print(v.length())
print(v.angle())
v2 = Vector2D(2, 4, 6, 8)
print(v, v2)
print(v + v2)
print(v - v2)
print(v.scalar_mul(v2))
