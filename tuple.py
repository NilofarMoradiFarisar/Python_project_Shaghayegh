# point = (1, 2)
point = (1,)
# 1,
# ()
# print(type(point))
# point_1 = ("2, 3, 6, 9", "a")
# point_2 = ("7, 2, 9, 7", "b")
# point_3 = point_1 + point_2
# point_3 = point_1 * point_2
# print(point_3)

point_1 = (1, 3, 5, 7)
point_2 = (2, 5, 7, 8)
point_3 = tuple(a * b for a, b in zip(point_1, point_2))
print(point_3)


print(tuple("python"))
print(tuple(range(4)))
print(point_1[2])

for i in enumerate(point_1):
    print(i)

# unpacking, Packing

point_1 = (1, 3, 5, 7)
x, y, *other = (1, 3, 5, 7)
print(x, y)
point = (1, 3, 5)
point[1] = 10 # incorrect
print(point)


