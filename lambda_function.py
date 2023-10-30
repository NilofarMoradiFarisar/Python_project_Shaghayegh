def add(a, b):
    return a + b
print(add(2, 3))

# cal_add = add(2, 3)


add = lambda a, b, c : a + b * c
print(add(2, 5, 6))

multiple = lambda r, n : r * n
print(type(multiple))

def multiple(r, n=0):
    return r * n 