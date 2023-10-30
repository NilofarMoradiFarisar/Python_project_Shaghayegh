
{}
{key_1: value_1, key_2: value_2, key_3: value_3}
list()
set()
tuple()
array()

dict()
point = dict(x=1, y=2)
print(point)
print(type(point))


point = {'x': 1, 'y': 2}
print(point['x'])
point['x'] = 3

point['z'] = 5
# print(point)

print(point.get('p', 8))
# print(point['p'])
del (point['x'])
print(point)

# for i in range(3):
# print(i)


point = {'x': 1, 'y': 2}


for key, value in point.items():
    print(key, value)
    print(type(key))
'''
for key in point.keys():
    print(key)
    print(type(key))

for value in point.values():
    print(value)
    print(type(value))

for key, value in point.items():
    print(key, value)

for key in point.items():
    print(key)
    print(type(key))
    '''
