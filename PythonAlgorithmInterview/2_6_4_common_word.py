# 가장 흔한 단어
# 금지 된 단어를 제외한 가장 흔하게 등장하는 단어를 출력, 대소문자를 구분하지 않으며 구두점 또한 무시
import collections
import re

def solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    print(words)
    
    count = collections.Counter(words)
    print(count)



if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    
    solution(paragraph, banned)