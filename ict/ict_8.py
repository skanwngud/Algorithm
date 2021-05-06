# 왕실의 나이트

# 행 1 ~ 8, 열 a ~ h
# 수직으로 2칸 이동 후 수직으로 1 칸, 수평으로 2칸 이동 후 수평으로 1칸 이동 가능

'''
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
        '''

# 영상 해답
# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 움직일 수 있는 방향벡터
# dx, dy 를 따로 지정하지 않고도 사용 가능
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 총 여덟가지

# 각 위치로 이동이 가능한지에 대한 판단
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)