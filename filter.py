# filter
# filter()

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


prices = []
for item in items:
    if item[1] >= 10:
        prices.append(item[1])

print(prices)

x = list(filter(lambda item: item[1] >= 10, items))
print(type(x))

for item in x:
    print(item)


filterd = list(filter(lambda item: item[1] >= 10, items))
print(filterd)