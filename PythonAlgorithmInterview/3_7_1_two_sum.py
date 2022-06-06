# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

def solution(nums, target):
    for idx in range(len(nums)):
        num = target - nums[idx]

        if num in nums[idx:]:
            return [idx, nums[idx + 1:].index(num) + (idx + 1)]
            
            
def solution2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
            
class Solution:
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
            
            
class SolutionKey:
    def twoSum(slef, nums, target):
        nums_map = {}
        
        # 키와 값을 바꿔 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
            
            
class SolutionAdjust:
    def twoSum(self, nums, target):
        nums_map = {}
        
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            
            nums_map[num] = i
            
            
class SolutionTwoPointer:
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
                
            else:
                return [left, right]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    nums2 = [-1, -2, -3, -4, -5]
    target2 = -8
    
    print(solution(nums, target))
    print(solution(nums2, target2))
    
    print(solution2(nums, target))
    print(solution2(nums2, target2))
    
    a = Solution()
    
    print(a.twoSum(nums, target))
    print(a.twoSum(nums2, target2))
    
    b = SolutionKey()
    
    print(b.twoSum(nums, target))
    print(b.twoSum(nums2, target2))
    
    c = SolutionTwoPointer()
    
    print(c.twoSum(nums, target))
    print(c.twoSum(nums2, target2))  # 해당 문제는 투 포인터로 풀 수 없다. (리스트가 정렬 되어있지 않기 때문)