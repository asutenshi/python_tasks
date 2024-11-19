class IPAddress():
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            if len(ipaddress.split('.')) == 4 and all([0<=x<=255 for x in list(map(int, ipaddress.split('.')))]):
                self.__ipaddress = [x for x in list(map(int, ipaddress.split('.')))]
            else: raise ValueError('Неправильно введён ipaddress')
        elif isinstance(ipaddress, (list, tuple)):
            if len(ipaddress) == 4 and all([0<=x<=255 for x in ipaddress]):
                self.__ipaddress = [x for x in ipaddress]
            else: raise ValueError('Неправильно введён ipaddress')
        else: return NotImplemented

    def __repr__(self):
        return f'IPAddress(\'{self.__ipaddress[0]}.{self.__ipaddress[1]}.{self.__ipaddress[2]}.{self.__ipaddress[3]}\')'
    def __str__(self):
        return f'{self.__ipaddress[0]}.{self.__ipaddress[1]}.{self.__ipaddress[2]}.{self.__ipaddress[3]}'

ipaddress = IPAddress('192.158.1.38')
ipaddress2 = IPAddress([192, 196, 0, 1])
ipaddress3 = IPAddress((255, 255, 255, 255))
print(ipaddress)
print(ipaddress2)
print(repr(ipaddress))
print(repr(ipaddress2))
