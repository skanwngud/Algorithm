# 그룹 아나그램
# 문자열 배열은 받아 애너그램 단위로 그룹핑하라

import collections

def solution(strs):
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        print(anagrams)
    
    return list(anagrams.values())
        
if __name__ == "__main__":
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution(input))
    
    # 정렬 방법
    
    a = [2, 5, 1, 9, 7]  # 숫자 정렬
    print(sorted(a))  # [1, 2, 5, 7, 9]
    
    b = 'zbdaf'  # 문자열 정렬
    print(sorted(b))  # ['a', 'b', 'd', 'f', 'z']
    print("".join(sorted(b)))  # 정렬 된 상태에서 다시 문자열로 만듦 'abdfz'
    
    # sorted 말고 list 형에는 sort 도 존재하나 이는 return 값이 None 이다.
    # 사용방법은 alist.sort()
    
    c = ['ccc', 'aaaa', 'd', 'bb']  # sorted key 값으로 정렬
    print(sorted(c, key=len))  # ['d', 'bb', 'ccc', 'aaaa']
    
    d = ['cde', 'cfc', 'abc']  # 함수를 이용한 정렬
    def fn(s):
        return s[0], s[-1]    # 첫 문자열과 마지막 문자열을 return 하는 함수
    print(sorted(d, key=fn))  # 첫 번째 문자열을 비교하고 값이 같으면, 그 다음 문자열을 비교한다. ['abc', 'cfc', 'cde']
    print(sorted(d, key=lambda x:(x[0], x[-1])))  # 위의 함수를 람다식으로 변경