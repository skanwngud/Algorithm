# 로그파일 재정렬
"""
1. 로그의 가장 앞 부분은 식별자.
2. 문자로 구성 된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
"""
def soultion(string):
    result_list = []
    
    letter_list = []
    digi_list = []
    
    for idx in range(len(string)):
        string_id = string[idx].split(" ")[0]
        
        if string_id[:3] == "let":
            letter_list.append(string[idx])
        else:
            digi_list.append(string[idx])
    
    print(letter_list)
    print(digi_list)
        
    result_list.append(letter_list)
    result_list.append(digi_list)
    
    return result_list
if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 arg can", "dig2 3 6", "let2 own kit dig", "let3 arg zero"]
    
    soultion(logs)