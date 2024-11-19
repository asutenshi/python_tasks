class Counter():
    def __init__(self, start=0):
        self.__value = start

    def inc(self, n=1):
        if isinstance(n, int):
            self.__value += n
        else:
            return NotImplemented

    def dec(self, n=1):
        if isinstance(n, int):
            if self.__value - n >= 0:
                self.__value -= n
            else:
                self.__value = 0
        else:
            return NotImplemented

class NonDecCounter(Counter):
    def __init__(self, start=0):
        Counter.__init__(self, start)

    def dec(self, n=1):
        pass

