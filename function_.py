'''
def add(x, y):
    print(f"{x} + {y}")


print(add(2, 3))
# add(2)


def add_multiple():
    print("Hi")
    print("World")
    print("!")


#######
def add(x=0, y=1):
    return x + y



def greeting(firstname):
    return f"hi {firstname}"


message = greeting("nilofar")
print(message)

--------------------------



def greeting(firstname, secondname="Moradi", age="?"):
    return f"hi {firstname} {secondname} you have {age}"


message = greeting("nilofar")
print(message)


#######################
'''


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number  # total = tatal * number
    return total


result = multiply(2, 3, 6, 8, 10)
print(result)



