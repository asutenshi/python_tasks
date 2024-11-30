from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        if isinstance(horizontal, str) and 'a' <= horizontal <= 'h' \
            and isinstance(vertical, int) and 1 <= vertical <= 8:
            self._horizontal = horizontal
            self._vertical = vertical
        else: raise ValueError('Неправильно введены координаты')

    @abstractmethod
    def can_move(self):
        pass

    def __str__(self):
        pass

class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        ChessPiece.__init__(self, horizontal, vertical)

    def can_move(self, horizontal, vertical):
        if isinstance(horizontal, str) and 'a' <= horizontal <= 'h' \
            and isinstance(vertical, int) and 1 <= vertical <= 8:
            h_diff = abs(ord(horizontal) - ord(self._horizontal))
            v_diff = abs(vertical - self._vertical)
            return (h_diff in (1, 0) and v_diff in(1, 0)) and not (h_diff == 0 and v_diff == 0)
        else: raise ValueError('Неправильно введены координаты')

    def __str__(self):
        return f'King({self._horizontal}, {self._vertical})'

class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        ChessPiece.__init__(self, horizontal, vertical)

    def can_move(self, horizontal, vertical):
        if isinstance(horizontal, str) and 'a' <= horizontal <= 'h' \
            and isinstance(vertical, int) and 1 <= vertical <= 8:
            h_diff = abs(ord(horizontal) - ord(self._horizontal))
            v_diff = abs(vertical - self._vertical)
            return ((h_diff == 2 and v_diff == 1) or (h_diff == 1 and v_diff == 2)) and not (h_diff == 0 and v_diff == 0)
        else: raise ValueError('Неправильно введены координаты')

    def __str__(self):
        return f'Knight({self._horizontal}, {self._vertical})'

figures = [King('b', 2), Knight('f', 4), King('h', 5), Knight('e', 8)]

for figure in figures:
    for h in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        for v in (1, 2, 3, 4, 5, 6, 7, 8):
            if figure.can_move(h, v):
                print(figure, f'can move to ({h}, {v})')
            else: print(figure, f'can\'t move to ({h}, {v})')
