# 최댓값 찾기
# 본인 풀이
import numpy as np
a = [17, 92, 18, 33, 58, 7, 33, 42]

def find_max(n):
    b = np.sort(n)
    return b[-1]

# 책 해답
def find_max2(a):
    n = len(a)
    max_v = a[0] # 최초 변수 선언
    for i in range(len(a)):
        if a[i] > max_v: # 조건문을 사용해 최초 변수와 비교
            max_v = a[i] # 비교 후 값이 더 큰 경우 변수를 다시 선언함
    return max_v

print(find_max(a)) # 92
print(find_max2(a)) # 92

# 최댓값의 위치를 찾는 알고리즘
# 본인 풀이(index 는 구글링 함)
def find_max_location(n):
    b = np.sort(n)
    b = b[-1]
    for i in range(len(n)):
        if b == n[i]:
            return n.index(n[i])

# 책 해답
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]: # 최초 a[1] 과 a[0] 을 비교했을 때 a[1] 이 크면 max_idx 는 1 이 되므로 다음에 비교 할 때는 a[2] 와 a[1] 이 된다.
            max_idx = i       # 그러나 두 번째에 비교했을 땐 a[2] > a[1] 이 성립 되지 않으므로 max_idx 는 그대로 1 이 된다.
    return max_idx

print(find_max_location(a)) # 1
print(find_max_idx(a)) # 1

# 연습문제
# 최솟값을 구하는 프로그램
def find_min(n):
    b = np.sort(n)
    return b[0]

def find_min_book(n):
    a = len(n)
    min_v = 0
    for i in range(a):
        if n[i] < n[min_v]:
            min_v = i
    return min_v

print(find_min(a)) # 7