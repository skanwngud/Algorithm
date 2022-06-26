# 배열을 입력받아 합으로 0 을 만들 수 있는 3개의 엘리먼트를 출력하라.abs(

class Solution:
    def solution(self, nums):
        reult_list = []
        
        for i in nums:
            for j in nums:
                for k in nums:
                    if i + j + k == 0:
                        print(i, j, k)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    
    a = Solution()
    a.solution(nums)