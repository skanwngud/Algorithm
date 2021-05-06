# 키패드
import numpy as np

number = [1, 2, 3, 4, 5]
hand = ['right', 'left']

numbers = np.arange(1, 10)
num_list = list()
for i in range(1, 5):
    for j in range(1, 4):
        temp = (i, j)
        num_list.append(temp)

print(num_list)

# if hand == 'right' and number == 2 or 5 or 8 or 0:
#     if 