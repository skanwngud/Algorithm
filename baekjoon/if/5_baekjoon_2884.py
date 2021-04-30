# 시계 45분 앞으로

H = 10
M = 10
time = str(H) + ':' + str(M)
print(str(H) + '\t' + str(M))

if M > 59:
    H += 1
elif M <0:
    H -= 1

print(time)