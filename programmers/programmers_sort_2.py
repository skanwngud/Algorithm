# 가장 큰 수

def solution(numbers):
    answer = ''
    temp = list(map(str, numbers))
    temp.sort(key=lambda x:x*3, revers=True)
    answer = str(int(''.join(temp)))
    return answer