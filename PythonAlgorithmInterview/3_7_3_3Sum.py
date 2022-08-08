# 배열을 입력받아 합으로 0 을 만들 수 있는 3개의 엘리먼트를 출력하라.
# 중복은 x

class Solution:
    def solution(self, nums):
        reult_list = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i:])):
                for k in range(len(nums[j:])):
                    if nums[i] + nums[j] + nums[k] == 0:
                        print(nums[i], nums[j], nums[k])

    def solution2(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j +1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results


    def two_pointer_solution(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):  # j, k 와의 중복을 피하기 위해 i 의 범위를 제한한다
            if i > 0 and nums[i] == nums[i - 1]:  # 중복값 건너뛰기
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:  # sum 이 0 보다 작으므로 포인터를 한 칸 이동해 값을 키운다
                    left += 1
                elif sum > 0:  # sum 이 0 보다 크므로 포인터를 한 칸 이동해 값을 줄인다
                    right -= 1
                else:  # sum == 0
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    
    a = Solution()
    print(a.solution2(nums))
    print(a.two_pointer_solution(nums))
