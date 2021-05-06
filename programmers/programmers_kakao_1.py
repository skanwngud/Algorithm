# 키패드
import numpy as np

# 본인풀이
'''
number = [1, 2, 3, 4, 5]
hand = ['right', 'left']

numbers = np.arange(1, 10)
num_list = dict()

for i in range(1, 5):
    for j in range(1, 4):
        for k in range(1, 13):
            temp = (i, j)
            num_list[k] = temp

print(num_list)

# if hand == 'right' and number == 2 or 5 or 8 or 0:
#     if 
'''

# 해답 풀이
def solution(numbers, hand):
    answer = ''
    left_hand = 10 # 키패드 위치 ( * 의 경우 )
    right_hand = 12 # 키패드 위치 ( # 의 경우 )
    for i in numbers:
        if i in [1, 4, 7]: # 1, 4, 7 의 경우는 무조건 왼손
            answer += 'L'
            left_hand = i
        elif i in [3, 6, 9]: # 3, 6, 9 의 경우는 무조건 오른손
            answer += 'R'
            right_hand = i
        else: # 2, 5, 8, 0 의 경우는 각 손끼리의 거리에 따라 결정
            i = 11 if i == 0 else i

            left_abs = abs(i - left_hand)
            right_abs = abs(i - right_hand)

            if sum(divmod(left_abs, 3)) > sum(divmod(right_abs, 3)): # divmod : 몫과 나머지를 튜플의 형태로 반환한다
                answer += 'R' # 마지막 손의 위치와 현재 숫자간의 거리가 오른손이 더 가까운 경우
                right_hand = i
            elif sum(divmod(left_abs, 3)) < sum(divmod(right_abs, 3)): # 마지막 손의 위치와 현재 숫자간의 거리가 왼손이 더 가까운 경우
                answer += 'L'
                left_hand = i
            else: # 마지막 손의 위치와 현재 숫자간의 거리가 동일한 경우
                if hand == 'left':
                    answer += 'L'
                    left_hand = i
                else :
                    hand == 'right'
                    answer += 'R'
                    right_hand = i
    return answer

