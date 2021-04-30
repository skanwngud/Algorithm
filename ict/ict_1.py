# 거스름돈 계산

# 본인 풀이
def change(n):
    temp = n // 500
    n = n - temp * 500
    temp2 = n // 100
    n = n - temp2 * 100
    temp3 = n // 50
    n = n - temp3 * 50
    temp4 = n // 10
    print(' 500 : %s\n'%temp, '100 : %s\n'%temp2, '50 : %s\n'%temp3, '10 : %s\n'%temp4)

# 강의 풀이
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)



print(change(1260))

# answer
#  500 : 2
#  100 : 2
#  50 : 1
#  10 : 1