try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didnot enter a valid age")
else:
    print("No exception where thrown")



try:
    file = open("content.txt")
    age = int(input("Age: "))
    xfactor = 10/age
    file.close()
except (ValueError, ZeroDivisionError):
    print("you didnot enter a valid age")
else:
    print("No exception where thrown")

try:
    file = open("content.txt")
    age = int(input("Age: "))
    xfactor = 10/age
    
except (ValueError, ZeroDivisionError):
    print("you didnot enter a valid age")
    file.close()
else:
    print("No exception where thrown")
    file.close()

try:
    file = open("content.txt")
    age = int(input("Age: "))
    xfactor = 10/age
    
except (ValueError, ZeroDivisionError):
    print("you didnot enter a valid age")
    file.close()
else:
    print("No exception where thrown")


try:
    file = open("content.txt")
    age = int(input("Age: "))
    xfactor = 10/age
    
except (ValueError, ZeroDivisionError):
    print("you didnot enter a valid age")
else:
    print("No exception where thrown")
finally:
    file.close()

