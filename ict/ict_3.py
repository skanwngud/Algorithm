# 각 자릿수를 연산하여 가장 큰 수를 출력
# 본인 풀이

n = str(2024)

def ict(n):
    for i in range(len(n)):
        if n[i] <= 1:
            n[i + 1] += n[i]



# 강의 해답
data = str(204)

result = int(data[0]) # 문자열 데이터를 정수형태로 변환

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
print(len(data))