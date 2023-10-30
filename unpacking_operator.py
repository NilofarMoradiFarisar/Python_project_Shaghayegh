numbers_1 = [1, 2, 3]
numbers_2 = [11, 12, 14]
# number = numbers_1 + numbers_2
number = [*numbers_1, *numbers_2]
print(number)
'''
print(numbers)
print(numbers[0], numbers[1], numbers[2])
print(*numbers)


values = list(range(5))  # = [range(5)]
print(values)
print(*range(5))

sal = "python"
print(*sal)
print([*sal])
'''
dictionary_1 = {"x": 1, "y": 2}
dictionary_2 = {"u": 1, "z": 2}
# dictionary = dictionary_1 + dictionary_2
# print(dictionary)
print({**dictionary_1, **dictionary_2})


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {k: v for d in [d1, d2] for k, v in d.items()}
print(d3) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}