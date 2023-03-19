stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

i = 0
for keys1 in stock.keys():
    for keys2 in prices.keys():
        if keys1 == keys2:
            i += stock[keys1] * prices[keys2]
print(i)