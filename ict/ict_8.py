# 왕실의 나이트

# 행 1 ~ 8, 열 a ~ h
# 수직으로 2칸 이동 후 수직으로 1 칸, 수평으로 2칸 이동 후 수평으로 1칸 이동 가능

# 본인 풀이
x, y = 0, 0 # 나이트 초기 위치
n = int(input())
plans = input().split()

# 방향 벡터
dx = [0, 0, -2, 2]
dy = [-2, 2, 0, 0]
move = ['1', '2', '3', '4']

print(plans)
print(type(plans))

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        