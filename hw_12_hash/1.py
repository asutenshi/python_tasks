def rabinKarpAlgorithm(t, p):
    print(t, p)
    n = len(t)
    m = len(p)
    list_i = []
    x = 5222869

    def single_hash(ch, i):
        return ord(ch) * x**i

    def hash(p):
        h = 0
        for i, ch in enumerate(p):
            h += single_hash(ch, i)
        return h

    p_hash = hash(p)

    i = n - m
    h = hash(t[i:i+m])
    while i >= 0:
        if p_hash == h:
            if t[i:i+m] == p: list_i.append(i)
        h -= single_hash(t[i+m-1], m-1)
        h *= x
        i -= 1
        h += single_hash(t[i], 0)
    return list_i[::-1]
print(rabinKarpAlgorithm('abacaba', 'aba'))
print(rabinKarpAlgorithm('restTesttesT', 'Test'))
print(rabinKarpAlgorithm('baaaaaaa', 'aaaaa'))
