class Father():
    def __init__(self, mood='neutral'):
        if isinstance(mood, str):
            if mood: self._mood = mood
            else: raise ValueError('Настроение не может быть пустой строкой')
        else: return NotImplemented

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self._mood = 'strict'

class Mother():
    def __init__(self, mood='neutral'):
        if isinstance(mood, str):
            if mood: self._mood = mood
            else: raise ValueError('Настроение не может быть пустой строкой')
        else: return NotImplemented

    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self._mood = 'kind'

class Daughter(Mother, Father):
    def __init__(self, mood='neutral'):
        Mother.__init__(self, mood)

class Son(Father, Mother):
    def __init__(self, mood='neutral'):
        Father.__init__(self, mood)

f = Father()
f.be_strict()
m = Mother()
m.be_kind()
d = Daughter()
d.be_strict()
s = Son()
s.be_kind()
for p in (f, m, d, s):
    print(p.greet())
