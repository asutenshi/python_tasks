l_names = ['fadsfasd', 'reqw', 'oiyvxc', 'oiurqmnxc']

def postphics(func):
    def add_postphics(l_names, book_name):
        for _, name in enumerate(l_names):
            print(f'{name}:{book_name}')
    return add_postphics

        
@postphics
def characters_names(l, book_name):
    return l, book_name

characters_names(l_names, 'qqq')