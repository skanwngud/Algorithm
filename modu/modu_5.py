# 재귀함수
# 1부터 n 까지의 곱을 구하라

# 본인 풀이
def pac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# 책 해답
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= 1
    return res

print(pac(5))
print(fact(5))