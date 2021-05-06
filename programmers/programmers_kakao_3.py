# 보석 쇼핑

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    num = 0
    answer = list()
    gem = list()
    for i in gems:
        if i == gems[num]:
            gem.append(i)
        else:
            pass
        num += 1
    return answer

print(solution(gems))

for g in zip(gems):
    if g != gems:
        print(g)