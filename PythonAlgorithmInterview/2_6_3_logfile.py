# 로그파일 재정렬
"""
1. 로그의 가장 앞 부분은 식별자.
2. 문자로 구성 된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
"""
def soultion(string):
    result_list = []  # 결과 리스트
    
    letter_list = []  # 문자 리스트
    digi_list = []  # 숫자 리스트
    
    for idx in range(len(string)):  # 입력값을 순회
        string_id = string[idx].split(" ")[0]  # 빈칸을 기준으로 split 한 값 (식별자)
        
        if string_id[:3] == "let":  # 식별자가 let (문자) 이면
            letter_list.append(string[idx])  # letter_list 에 append
        else:                       # 식별자가 dig (숫자) 이면
            digi_list.append(string[idx])  # digit_letter 에 append
    
    result_list = letter_list + digi_list  # 두 리스트를 + 연산
    
    return result_list

# 위 함수는 문제에 대한 제대로 된 이해가 결여 되어있어 풀이가 틀렸음.


class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
        
if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 arg can", "dig2 3 6", "let2 own kit dig", "let3 arg zero"]
    
    soultion(logs)
    
    a = Solution()
    print(a.reorderLogFiles(logs))