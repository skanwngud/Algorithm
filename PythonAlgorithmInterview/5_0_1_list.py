a = [1, 2, 3]  # list

"""
len(a) == O(1)
a[i] == O(1)
a[i:j] == O(k)
elem in a == O(n)
a.count(elem) == O(n)
a.index(elem) == O(n)
a.append(elem) == O(1)
a.pop() == O(1)
a.pop(0) == O(n)
del a[i] == O(n) // n 에 따라 다르다. 최악의 경우 O(n) 이다.
a.sort() == O(n lon n)
min(a), max(a) == O(n)
a.revers() == O(n)
"""