a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for k, v in a.items():
    print(k, v)
    
del a['key2']

print(a)

import collections

b = collections.defaultdict(int)  # default 값 지정
b['A'] = 5
b['B'] = 3

print(b)

b['C'] += 1
print(b)

c = [1, 2, 3, 4, 2, 4, 4, 6, 6, 5]
d = collections.Counter(c)  # 리스트 요소와 그 갯수를 dict 형태로 출력
print(d)
print(d.most_common(2))  # 최빈값 2개 출력