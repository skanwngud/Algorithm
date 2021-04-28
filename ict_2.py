# n 이 1 이 될 때까지의 수

# n / k 가 성립 안 될 시 n - 1
# n / k 가 성립 될 시 n / k
# 위 연산 반복

# 본인 풀이
def ict(n, k):
    count = 0
    res = 0
    while res == 1:
        if n % k == 0:
            res = n/k
            count += 1
            print(res)
        elif n % k != 0:
            res = n -1
            count += 1
            print(res)
    return count

print(ict(25, 5))

# 강의 해답
# n, k = map(int, input().split())

results = 0
n = 25
k = 3

while True:
    # n 이 k 로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k       # n 이 k 로 나누어떨어지는 가장 가까운 수를 구할 수 있음
    results += (n-target)
    n = target
    # n 이 k 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    results += 1
    n //= k

# 마지막으로 나온 수에서 1 씩 빼기 반복
results += (n-1)
print(results)