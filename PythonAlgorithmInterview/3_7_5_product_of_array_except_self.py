# 배열을 입력받아 output[i] 가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
# 나눗셈을 하지 않고 O(n) 에 풀이하라.

class Solution:
    def solution(self, nums):
        res = []
        for idx in range(len(nums)):
            res.append([v for i, v in enumerate(nums) if idx != i])

    def solution2(self, nums):
        results = []

        p = 1
        for idx in range(len(nums)):
            results.append(p)
            p *= nums[idx]

        p = 1
        for idx in range(len(nums) - 1, -1, -1):
            results[idx] = results[idx] * p
            p *= nums[idx]

        return results

if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    a = Solution()
    a.solution(nums)
    print(a.solution2(nums))

    for idx in range(len(nums) - 1, -1, -1):
        print(idx)