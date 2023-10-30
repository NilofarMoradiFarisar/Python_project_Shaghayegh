from sys import getsizeof

numbers = [i*2 for i in range(100000)]
print("list", getsizeof(numbers))
print(len(numbers))

numbers = (i*2 for i in range(100000))
print("generator", getsizeof(numbers))
print(len(numbers))
'''
numbers = [16, 12, 13]

# generators_object
numbers = (i*2 for i in range(5))
print(type(numbers))


print(numbers)
for x in numbers:
    print(x, type(x))


print(range(5))
for i in range(5):
    print(i, type(i))
'''
