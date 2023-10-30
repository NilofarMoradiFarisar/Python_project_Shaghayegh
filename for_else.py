# successful = True

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("attempt 3 times failed")

print("done!")