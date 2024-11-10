class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name: self.name = name
        else: raise ValueError('Некорректное имя')
        if isinstance(age, int) and 0 <= age <= 110: self.age = age
        else: raise ValueError('Некорректный возраст')

user = User(None, None)
