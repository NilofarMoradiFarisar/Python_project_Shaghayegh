# numbers = []

# for x in range(5):
# numbers.append(x*2)

# print(numbers)

# list_comprehension

numbers = [i*2 for i in range(5)]
print(type(numbers))

numbers = {x: x*2 for x in range(5)}
print(numbers)


# list_comprehension


[item[1] for item in items]
list(map(lambda item: item[1], items))

[item[1] for item in items if item[1] >= 10]
list(filter(lambda item: item[1] >= 10, items))