# 구현 문제
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야하는 문제
# 적절한 라이브러리를 찾아서 사용해야하는 문제

for i in range(5):
    for j in range(5):
        print('(', i, ',', j,')', end = '')
    print()


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x,y = [2, 2]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)