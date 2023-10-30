letters = ["a", "b", "d", "d", "c"]
'''
# letters.append("u")
# letters.insert(3, "p")
# letters.pop()
# letters.pop(1)
# letters.remove("a")
print(letters.index("a"))
letters.count("d")
print(letters.count("d"))
# print(letters.index("h"))
if "d" in letters:
    print(letters.count("d"))

################
letters.sort(reverse=True)
print(letters)
# .sort()
print(sorted(letters))
'''
del letters[0]
letters.clear()
print(letters)
# Incomplete
