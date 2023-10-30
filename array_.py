from array import array
number = ["i", 12, 15, 16]
print(type(number))
numbers = array("i", [12, 15, 16])
print(numbers)
print(type(numbers))
b = ("i", [12, 15, 16])
print(type(b))

numbers_class = [[1, 2, 3, 4]]  # o(1)
numbers_class = [[1, 2, 3, 4], [1, 2, 3, 4]]  # o(2)