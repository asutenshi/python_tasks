class Product():
    def __init__(self, name, price, weight):
        # хранить цену будем в копейках, а вес в граммах
        if isinstance(name, str) and isinstance(price, int) and isinstance(weight, int):
            if name: self.__name = name
            else: raise ValueError('Имя не может быть пустой строкой')
            if price >= 0: self.__price = price
            else: raise ValueError('Цена не может быть отрицательной')
            if weight > 0: self.__weight = weight
            else: raise ValueError('Вес не может быть отрицательным числом или равным 0')
        else: return NotImplemented

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if new_name: self.__name = new_name
            else: raise ValueError('Имя не может быть пустой строкой')
        else: return NotImplemented

    @property
    def price(self): return self.__price
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int):
            if new_price >= 0: self.__price = new_price
            else: raise ValueError('Цена не может быть отрицательной')
        else: return NotImplemented

    @property
    def weight(self): return self.__weight
    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, int):
            if new_weight > 0: self.__weight = new_weight
            else: raise ValueError('Вес не может быть отрицательным числом или равным 0')
        else: return NotImplemented

class Buy(Product):
    # логически в этом классе не должно быть сеттеров для рассчитанных значений, поэтому я их напишу, но закоментирую
    def __init__(self, product, quantity):
        if isinstance(product, Product) and isinstance(quantity, int):
            if quantity > 0:
                self.__count = quantity
            else: raise ValueError('Количество не может быть отрицательным или равным нулю')
            self.__product = product
            self.__totalPrice = quantity * product.price
            self.__totalWeight = quantity * product.weight

    def __update(self):
        self.__totalPrice = self.__count * self.__product.price
        self.__totalWeight = self.__count * self.__product.weight

    @property
    def count(self): return self.__count
    @count.setter
    def count(self, new_count):
        if isinstance(new_count, int):
            if new_count > 0: 
                self.__count = new_count
                self.__update()
            else: raise ValueError('Количество не может быть отрицательным или равным нулю')
        else: return NotImplemented

    @property
    def product(self): return self.__product
    @product.setter
    def product(self, new_product):
        if isinstance(new_product, Product):
            self.__product = new_product
            self.__update()
        else: return NotImplemented


    @property
    def totalPrice(self): return self.__totalPrice
    # @totalPrice.setter
    # def totalPrice(self, new_totalPrice):
    #     if isinstance(new_totalPrice, int):
    #         if new_totalPrice >= 0: self.__totalPrice = new_totalPrice
    #         else: raise ValueError('Цена не может быть отрицательной')
    #     else: return NotImplemented

    @property
    def totalWeight(self): return self.__totalWeight
    # @totalWeight.setter
    # def totalWeight(self, new_totalWeight):
    #     if isinstance(new_totalWeight, int):
    #         if new_totalWeight > 0: self.__totalWeight = new_totalWeight
    #         else: raise ValueError('Вес не может отрицательным или равным нулю')
    #     else: return NotImplemented

class Check(Buy):
    def __init__(self, buy):
        Buy.__init__(self, buy.product, buy.count)

    def __str__(self):
        return f'Product name: {self.product.name}\nProduct price: {self.product.price / 100} руб.\nProduct weight: {self.product.weight / 1000} кг.\nCount of products: {self.count}\nTotal Price: {self.totalPrice / 100} руб.\nTotal Weight: {self.totalWeight / 1000} кг.'

p = Product('колбаса', 100000, 500)
b = Buy(p, 8)
print(b.count, b.totalPrice, b.totalWeight)
ch = Check(b)
print(ch)
m = Product('мандарин', 30000, 100)
b.product = m
b.count = 30
print(b.count, b.totalPrice, b.totalWeight)
ch = Check(b)
print(ch)
