n = 3

# 본인 풀이
for i in range(1, n+1):
    i += i

print(i)

# 해답
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)