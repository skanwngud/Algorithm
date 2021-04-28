# 동명이인 찾기

s = ['tom', 'jerry', 'mike', 'tom']
s2 = ['tom', 'jerry', 'mike', 'tom', 'mike']

# 본인 풀이 (tom 만 인식하고 jerry 부터는 인식 못함)
def same_name(n):
    idx = 0
    for i in range(1, len(s)):
        if n[idx] == n[i]:
            return n[i]
        else:
            pass

# 책 해답
def find_same_name(a):
    n = len(a)
    results = set()                 # 이름을 저장한 집합 선언
    for i in range(0, n-1):         # 리스트 전체를 반복하는 것이 아닌 list[-1] 는 제외
        for j in range(i+1, n):     # 리스트 전체를 반복할 때 그 다음 순서와 비교
            if a[i] == a[j]:        # i 와 j, 즉 기준이 되는 부분과 그 다음 부분이 같다는 조건이면
                results.add(a[i])   # a[i] 번째의 이름을 집합에 올림
    return results

print(same_name(s2))                # 본인 풀이의 경우 제일 첫 번째에 있는 tom 이 중복 되는 경우만 인식
print(find_same_name(s2))

# 연습문제
s3 = ['tim', 'jerry', 'mike']

def pair(n):
    results = set()
    for i in range(0, len(n)-1):
        for j in range(i+1, len(n)):
            if n[i] != n[j]:
                a = (n[i] + ' - ' + n[j])
                results.add(a)
    return results

print(pair(s3))