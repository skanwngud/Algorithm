# 모험가 길드

# 본인 풀이
n = 5
boken = [2, 3, 1, 2, 2]

def ict(list):
    for i in range(len(list)):
        list.sort() # 오름차순으로 정렬
        print(list) # 정렬 되었는지 확인
        a = i + 1
        idx = list[i]
        guild = set()
        if a == idx:
            guild.add(a)
        else:
            # guild.add(idx[:i])
            pass
    return guild

print(ict(boken))

# 영상 해답
results = 0 # 총 그룹의 수
count = 0   # 현재 그룹에 포함 된 모험가의 수
boken.sort() # 오름차순으로 정렬

for i in boken: # 공포도가 낮은 것부터 하나씩 확인
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i: # 현재 그룹에 포함 된 모험가의 수가 현재의 공포도 이상이면, 그룹에 포함
        results += 1 # 총 그룹수 증가시키기
        count = 0 # 현재 그룹에 포함 된 모험가 수 초기화

print(results)