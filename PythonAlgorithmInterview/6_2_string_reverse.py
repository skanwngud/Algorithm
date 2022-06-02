# 문자열 뒤집기

def solution(string):
    reverse_string = string[::-1]
    print(reverse_string)
    
    
class SolutionSlicing:
    def reverseString(self, s):
        s = s[::-1]  # 공간복잡도가 O(1) 이므로 O(n) 은 안 된다.
        s[:] = s[::-1]  # 이건 가능
        
        
class SolutionReverse:
    def reverseString(self, s):
        s = s.reverse()
        

if __name__ == "__main__":
    s = list("hello")
    solution(s)
    
    a = SolutionSlicing()
    a.reverseString(s)
    
    a = SolutionReverse()
    a.reverseString(s)