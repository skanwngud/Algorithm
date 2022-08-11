# 연결 리스트가 팰린드롬 구조인지 판별하라

class Solution:
    def solution(self, nums):
        nums = list(nums)
        for idx in range(len(nums)):
            left = idx
            right = len(nums) - idx
            if nums[left] == nums[right]:
                continue
            else:
                return False
        return True

    def solution2(self, head):
        q = []

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

