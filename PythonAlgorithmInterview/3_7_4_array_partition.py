# n 개의 페어를 이용한 min(a, b) 의 합으로 만들 수 있는 가장 큰 수를 출력하라

class Solution:
    def ascending(self, nums):  # 오름차순으로 정렬 후 계산
        sum = 0
        nums.sort()

        nums = [[nums[i], nums[i+1]] for i in range(0, len(nums), 2)]

        for num in nums:
            sum += min(num)

        return sum

    def pair_sum(self, nums):
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return n

    def pythonic(self, nums):
        return sum(sorted(nums[::2]))


if __name__ == "__main__":
    input = [1, 4, 3, 2]

    a = Solution()
    print(a.ascending(input))
    print(a.pair_sum(input))
    print(a.pythonic(input))
