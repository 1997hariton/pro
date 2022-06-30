def pol(a):
    if len(a)<=1:
        return True
    if a[0]!=a[-1]:
        return False
    return pol(a[1:-1])
print(pol('шалаш'))
