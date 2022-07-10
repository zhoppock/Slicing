a = [1, 2, 3, 4, 5]
print(a)
a[2:] = []
print(a)
a.append(['d', 'e'])
print(a)
a.extend(['d', 'e'])
print(a)
a[len(a):] = ['d', 'e']
print(a)
a += 'de'
print(a)
a[2:4] = []
print(a)