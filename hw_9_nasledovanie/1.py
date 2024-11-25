class Counter():
    def __init__(self, start=0): self._value = start

    def inc(self, n=1):
        if isinstance(n, int): self._value += n
        else: return NotImplemented

    def dec(self, n=1):
        if isinstance(n, int):
            if self._value - n >= 0: self._value -= n
            else: self._value = 0
        else: return NotImplemented

    def __str__(self): return f'Counter(value = {self._value})'

class NonDecCounter(Counter):
    def __init__(self, start=0): Counter.__init__(self, start)

    def dec(self, n=1): pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.__limit = limit

    def inc(self, n=1):
        if isinstance(n, int):
                if self._value + n <= self.__limit: self._value += n
                else: raise ValueError("Счетчик не может превышать свой установленный лимит")
        else: return NotImplemented

    def __str__(self):
        return Counter.__str__(self) + f'(limit = {self.__limit})'

c = Counter(2)
ndc = NonDecCounter(3)
lc = LimitedCounter(4)

print(c)
c.inc(10)
print(c)
c.dec(1)
print(c)
print(ndc)
ndc.inc(10)
print(ndc)
ndc.dec(1)
print(ndc)
print(lc)
lc.inc(10)
print(lc)
lc.dec(1)
print(lc)


