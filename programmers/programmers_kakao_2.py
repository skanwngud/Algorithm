# 수식의 최대화
# 본인 풀이
import re

expression = '100-200*300-500+20'

result = 0

def cal_(a, b, ca):
    if ca == '+':
        return a + b
    elif ca == '-':
        return a - b
    else:
        return a * b

def solution(expression):
    cal = list()
    number = re.findall('\d+', expression)
    answer = 0
    
    for i in range(len(expression)):
        if expression[i].isdigit() == False:
            cal.append(expression[i])

    for i in range(len(number)):
        for j in range(len(cal)):
            answer += cal_(int(number[i]), int(number[i]), cal[j])
            print(answer)
    return answer

print(solution(expression))

# 정답 풀이
import re

from itertools import permutations

def solution2(expression):
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)', expression)

    a = list()
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                temp = _ex.index(y)
                _ex[temp-1] = str(eval(_ex[temp-1]+_ex[temp]+_ex[temp+1]))
                _ex = _ex[:temp]+_ex[temp+2:]
        a.append(_ex[-1])
    return max(abs(int(x)) for x in a)

print(solution2(expression))