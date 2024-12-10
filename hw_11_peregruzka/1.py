from functools import singledispatchmethod
from typing import Union

class Negator():
    def __init__(self):
        pass

    @singledispatchmethod
    def neg(self, arg) -> Union[int, float, bool]:
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int | float)
    def _(self, arg):
        if isinstance(arg, bool): return not arg # bool наследуется, от int ->
        # register(int) перехватывает значение раньше, чем register(bool). Но register(int)
        # не может вернуть bool, поэтому я переопределяю возвращаемые значения для neg.
        else: return -arg

n = Negator()
print(n.neg(12))
print(n.neg(True))
print(n.neg(-1.228))
print(n.neg([-1]))
