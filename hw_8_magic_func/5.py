class FoodInfo():
    def __init__(self, proteins, fats, carbohydrates):
        if isinstance(proteins, (int, float)) and isinstance(fats, (int, float)) and isinstance(carbohydrates, (int, float)):
            self._proteins = proteins
            self._fats = fats
            self._carbohydrates = carbohydrates
        else: return NotImplemented
    def __repr__(self):
        return f'FoodInfo({self._proteins}, {self._fats}, {self._carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo((self._proteins + other._proteins), (self._fats + other._fats), (self._carbohydrates + other._carbohydrates))
        else: return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo((self._proteins * n), (self._fats * n), (self._carbohydrates * n))
        else: return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo((self._proteins / n), (self._fats / n), (self._carbohydrates / n))
        else: return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo((self._proteins // n), (self._fats // n), (self._carbohydrates // n))
        else: return NotImplemented


food1 = FoodInfo(10, 15, 20)
food2 = FoodInfo(25, 56, 87)
print(food1)
print(food1 + food2)
print(food1 * 10)
print(food1 / 10)
print(food1 // 2)
