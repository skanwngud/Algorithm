# 연결 리스트가 팰린드롬 구조인지 판별하라
import collections


class Solution:
    def solution(self, nums):
        q = []

        node = nums
        while node is not None:
            q.append(node.val)
            node = node.next


        for idx in range(len(nums)):
            left = idx
            right = len(nums) - idx
            if nums[left] == nums[right]:
                continue
            else:
                return False
        return True

    def solution2(self, head):
        q = collections.deque()

        if head is None:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
               return False

        return True

    def solution3(self, head):
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

