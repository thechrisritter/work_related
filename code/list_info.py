# A simple code I used to collect simple data from thosands of items in two lists.
# Please feel free to help make this more Pythonic.
# I want to update this so that a and b pull from csv files instead of lists.
a = [1, 2, 3, 4]
b = [2, 3, 7, 8]

c = set(b) - set(a)
d = set(a) - set(b)
e = a + b

total = len(e)
matches = len(d)
unique = len(c)
a_total = len(a)
b_total = len(b)

print('Results:')
print(c)
print('List A total: ', a_total)
print('List B total: ', b_total)
print('Total: ', total)
print('Matches: ', matches)
print('Unique items: ', unique)
input()
