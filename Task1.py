a = input('Write your sentence here: ')
dict1 = {}
for i in list(a.split(' ')):
    dict1.update({i : a.count(i)})
print(dict1)