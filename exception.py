try:
    numbers = [1, 2]
    print(numbers[8])
except IndexError:
    print("Please enter number in range")

try:
    age = int(input("Please enter your age: "))
    print(10/age)
    print(age)
except ValueError:
    print("Error!!!", "Please print a number not charecter")
except ZeroDivisionError:
    print("enter a number more than zero")
