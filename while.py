# while True:

# while condition:

# for x in range(2):  # object iterable
# print(x)

comment = ""
while True:
    comment = input(">>>")
    print(comment)
    if comment.lower() == "exit":
        break
print("done!")
