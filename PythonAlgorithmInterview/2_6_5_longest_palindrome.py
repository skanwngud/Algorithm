# 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 부분 문자열을 출력하다

def solution(s):
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # 해당 사항이 없을 땐 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) -1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
        
    return result


if __name__ == "__main__":
    input1 = "babad"
    input2 = "cbbd"
    
    print(solution(input1))
    print(solution(input2))