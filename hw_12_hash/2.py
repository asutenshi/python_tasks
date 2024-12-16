class colorColoredPoint():
    def __init__(self, x=0, y=0, color='black'):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            if isinstance(color, str):
                if str:
                    self.__x = x
                    self.__y = y
                    self.__color = color
                else: raise ValueError('Цвет не может быть пустой строкой')
            else: return NotImplemented
        else: return NotImplemented

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def color(self):
        return self.__color

    def __repr__(self):
        return f'ColoredPoint(x={self.x}, y={self.y}, color={self.color})'

    def __eq__(self, other):
        if isinstance(other, colorColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        else: return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))

cp = colorColoredPoint(1, 2, 'red')
cp2 = colorColoredPoint(2, 2)
cp3 = colorColoredPoint(4, -2, 'green')
print(cp)
print(cp2.x, cp2.y, cp2.color)
print(cp != cp2)
dict_ = {cp:11, cp2:22, cp3:33}
for key, value in dict_.items():
    print(key, value)
