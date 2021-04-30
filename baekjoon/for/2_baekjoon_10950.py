A = 10
B = 30
T = 5

# 본인풀이
A, B = map(int, input().split())
T = int(input())

for i in range(T):
    print(A + B)

# 해답
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)