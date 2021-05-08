# 영어 숫자로

import re

s = 'onezero4seveneight'

# answer = 0
# num = list()
# alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# for i in alpha:
#     idx = 0
#     if i in s:
#         num.append(i)
#         if num[idx] == 'zero':
#             num[idx] = num[idx].replace('zero', '0')
#         elif num[idx] == 'one':
#             num[idx] = num[idx].replace('one', '1')
#         elif num[idx] == 'two':
#             num[idx] = num[idx].replace('two', '2')
#         elif num[idx] == 'three':
#             num[idx] = num[idx].replace('three', '3')
#         elif num[idx] == 'four':
#             num[idx] = num[idx].replace('four', '4')
#         elif num[idx] == 'five':
#             num[idx] = num[idx].replace('five', '5')
        
#     idx += 1        
# print(num)
def solution(s):
    answer = 0
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(10):
        p = s.replace(alpha[i], num[i])
        s = p
        answer = s
    print(type(answer))
    return int(answer)
print(solution(s))