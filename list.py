# list
'''numbers_1 = [12, 15, 18, 20]

x, y, *other = [12, 15, 18, 20]
print(x, y)

# number_1 = 12
# number_2 = 15
matrix = [[], []]
# print(numbers[0])
# print(numbers[2])
numbers_2 = [12, 15, 19, 22, 25]
conc_numbers = numbers_2 + numbers_1
print(conc_numbers)

# lists are iterable
print(range(2, 5))
for i in range(2, 5):
    print(i)
print(list(range(2, 5)))

print(list((2, 5)))

print(list("python"))

print(len(numbers_1))

numbers_1 = [1, 2, 3, 4]
print(numbers_1[1])
# print(type(numbers_1[1]))

print(numbers_1[-1])
print(numbers_1[-4])
print(numbers_1[:2])
# print(type(numbers_1[:2]))
print(numbers_1[1:2])
print(type(numbers_1[1:2]))
print(numbers_1[::2])

print("&")
print(numbers_1[:-1])
print(numbers_1[-4:])
print(numbers_1[-4:-2])
print(numbers_1[-2:-4])
print(numbers_1[::-1])
print(numbers_1[1::-1])
print("&")
print(numbers_1[3::-1])
print(numbers_1[2::-1])

print(numbers_1[::-2])
print(numbers_1[:5])
# -5 -4 -3 -2 -1 0 1 2 3 4 5

numbers_1 = [1, 2, 3, 4]
print(numbers_1[::-1])
print(numbers_1[::-2])
print(numbers_1[0::-1])
print(numbers_1[1::-1])
print(numbers_1[2::-1])
print(numbers_1[3::-1])
print(numbers_1[4::-1])
print(numbers_1[5::-1])

print(numbers_1[0:1:-1])
print(numbers_1[0:2:-1])

print(numbers_1[1:0:-1])
print(numbers_1[2:0:-1])
'''
'''
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
    print(type(number))


letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)
    print(type(letter))

# enumerate()
print(type(range(0)))
print(type(enumerate(letters)))

for letter in enumerate(letters):
    print(letter)



for letter in range(3):
    print(letter)
'''
letters = ["a", "b", "c", "d"]
for letter in enumerate(letters):
    # print(letter[1])
    print(letter[0], letter[1])


for letter in enumerate(range(3)):
    print(letter)
    print(letter[0])
    # print(type(letter))
