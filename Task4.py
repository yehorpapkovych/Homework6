days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print({days.index(i) + 1: i for i in days})
dict1 = {}
for i in days:
    dict1.update({i : days.index(i) + 1})
print(dict1)
# Why not? ;(
# print({i for i in days: days.index(i) + 1})
# print({days[ind] for ind in range(len(days)) : ind + 1 for ind in range(len(days))})