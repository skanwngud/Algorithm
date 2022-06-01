print(True == 1)
print(True == 0)
print(False == 1)
print(False == 0)

print(int(True))

a = 10
b = a
print(f"a = 10 : {id(a)}")
print(f"b = a: {id(b)}")
print(f"int 10: {id(10)}")
print(id(a) == id(b))
print(id(a) is id(b))

a = [1, 2, 3, 4]
print(id(a))
print(id([1, 2, 3, 4]))

b = a
a[1] = 0
print(id(b))
print(id(a))
print(id([1, 0, 3, 4]))