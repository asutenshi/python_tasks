# from functools import total_ordering
#
# @total_ordering
# если использовать total_ordering, то не получится возвращать NotImplemented
class Word():
    def __init__(self, word):
        if isinstance(word, str) and word:
            self._word = word
        else: raise ValueError('Неправильно введено слово')

    def __repr__(self):
        return f'Word(\'{self._word}\')'
    def __str__(self):
        return f'{self._word.capitalize()}'

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self._word) < len(other._word)
        else: return NotImplemented

    def __le__(self, other):
        if isinstance(other, Word):
            return len(self._word) <= len(other._word)
        else: return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self._word) > len(other._word)
        else: return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Word):
            return len(self._word) >= len(other._word)
        else: return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self._word) == len(other._word)
        else: return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Word):
            return len(self._word) != len(other._word)
        else: return NotImplemented



word = Word('tenshi')
word2 = Word('yami')
print(repr(word))
print(word >= '121')
