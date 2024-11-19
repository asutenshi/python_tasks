class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name: self.__name = name
        else: raise ValueError('Некорректное имя')
        if isinstance(age, int) and 0 <= age <= 110: self._age = age
        else: raise ValueError('Некорректный возраст')

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name: self.__name = new_name
        else: raise ValueError('Некорректное имя')

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 110: self._age = new_age
        else: raise ValueError('Некорректный возраст')


user = User('tenshi', 19)
print(user.get_name)
user.set_name = 'yami'
print(user.get_name)
print(user.get_age)
user.set_age = 20
print(user.get_age)
