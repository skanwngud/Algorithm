# 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

def solution(string):
    input_string = string
    input_string_list = list(input_string)
    
    reverse_string_list = [input_string_list[-idx -1] for idx in range(len(input_string_list))]
    
    for idx in range(len(input_string_list)):
        if input_string_list[idx] == reverse_string_list[idx]:
            return True
        
        else:
            return False
        


def solution(string):
    string_list = []
    
    for idx in string:
        if idx.isalnum():
            string_list.append(idx.lower())
            
    reverse_string_list = [string_list[-idx -1] for idx in range(len(string_list))]
    
    if string_list == reverse_string_list:
        return True
    
    else:
        return False

if __name__ == "__main__":
    print(solution("hello guys"))
    print(solution("A man, a plan, a canal: Panama"))