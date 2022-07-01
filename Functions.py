def add(a=0, b=0, c=0):
    return a + b + c

d = dict(b=6, c=5, a=7)
print(d)
print(add(**d))