# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로 이루어짐
# 모든 알파벳은 오름차순으로, 그 뒤에 모든 숫자를 더한 값을 출력

import numpy as np

data = 'K1KA5CB7'

# 본인풀이
# alphabet = list()
# digit = list()
# digit_label = np.arange(0, 10)

# for i in range(len(data)):
#     if type(data[i]) == int:
#         digit.append(data[i])
#     else:
#         alphabet.append(data[i])

# while True:
#     for i in range(len(data)):
#         if int(data[i]) == True:
#             digit.append(data[i])
#         else:
#             alphabet.append(data[i])
#     break

# print(data[0])
# print(ord(data[0]))
# print(data[1])
# print(ord(data[1]))
# print(digit_label)

# 영상 해답
result = list()
value = 0

for x in data:
    if x.isalpha(): # isalpha, isdigit : 해당 문자가 alphabet 인지 digit 인지 True, False 값으로 리턴해준다.
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))