# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
import sys


class Solution:
    def solution(self, nums):
        ptr = 0
        ptr_list = []
        for idx in range(1, len(nums)):
            if nums[ptr] > nums[idx]:
                ptr_list.append(ptr)
                ptr = idx

        if ptr == len(nums) - 1 and len(ptr_list):
            ptr = ptr_list[len(ptr_list)-1]

        best_time = max(nums[ptr:])
        return best_time - nums[ptr]

    def solution2(self, nums):
        if len(nums) == 1:
            return 0

        results = []
        ptr = 0
        while True:
            if ptr == len(nums) - 1:
                break

            results.append([nums[idx] - nums[ptr] for idx in range(ptr+1, len(nums))])
            ptr += 1

        results = [max(res) for res in results]
        return max(results) if max(results) >= 0 else 0

    def solution3(self, prices):
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

if __name__ == "__main__":
    # nums = [7, 1, 5, 3, 6, 4]
    # nums = [2, 4, 1]
    # nums = [3, 2, 6, 5, 0, 3]
    # nums = [7, 6, 4, 3, 1]
    nums = [1]

    a = Solution()
    # print(a.solution(nums))
    print(a.solution2(nums))
    print(a.solution3(nums))