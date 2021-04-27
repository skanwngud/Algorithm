# 1 ~ 10까지의 합
# 본인 풀이
def sum_110(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    return sum + b

# 책 해답
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

# 추가 책 해답
def sum_nn(n):
    return n*(n+1)//2

print(sum_110(1, 10)) # 55
print(sum_n(10)) # 55
print(sum_nn(10)) # 55

# 연습문제
def practice_1(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * i
    return sum

print(practice_1(10)) # 385

def practice_2(n):
    return n * (n+1) * (2 * n + 1) // 6

print(practice_2(10)) # 385