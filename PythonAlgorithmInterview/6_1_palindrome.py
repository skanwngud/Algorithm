# 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.


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


# list 로 반환
class SolutionList:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        # palindrome 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
            
        return True
    

# Deque를 이용한 방법
import collections
class SolutionDeque:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
    

# 파이썬의 최적화 (문자 슬라이싱)
import re
class SolutionPython:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
    
if __name__ == "__main__":
    print(solution("hello guys"))
    print(solution("A man, a plan, a canal: Panama"))
    
    string = SolutionList()
    print(string.isPalindrome("hello guys"))
    print(string.isPalindrome("A man, a plan, a canal: Panama"))
    
    string = SolutionDeque()
    print(string.isPalindrome("hello guys"))
    print(string.isPalindrome("A man, a plan, a canal: Panama"))
    
    string = SolutionPython()
    print(string.isPalindrome("hello guys"))
    print(string.isPalindrome("A man, a plan, a canal: Panama"))