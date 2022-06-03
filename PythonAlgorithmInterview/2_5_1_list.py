a = [1, 2, 3]
print(f'origin: {a}')

a.append(4)
print(f'append: {a}')

a.insert(4, 5)
print(f'insert: {a}')

a.append('Hello')
a.append(True)
print(f'other types add: {a}')

print(a[1:4:2])  # a[start:end:step]

del a[1]  # position
print(f'del: {a}')

a.remove(4)  # value
print(f'remove: {a}')

print(a.pop(3))  # position, delete after return value

