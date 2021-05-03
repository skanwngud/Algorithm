# 시각 (time)

# n = int(input())
n = 5

H = 10
M = 59
S = 59

# 본인 풀이
count = 0
for i in range(H):
    if i > 10:
        if str(i)[0] == 3:
            count+=1
        elif str(i)[1] == 3:
            count+=1
        else:
            pass
    elif i < 10:
        if str(i) == 3:
            count += 1
    for j in range(M):
        if str(j)[0] == 3:
            count += 1
        elif str(j)[1] == 3:
            count += 1
        for k in range(S):
            if str(k)[0] == 3:
                count += 1
            elif str(k)[1] == 3:
                count += 1
    print(count)

# 영상 해답
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
print(count)