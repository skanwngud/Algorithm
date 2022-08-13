# 두 정렬 리스트의 병합

class Node:  # Node vertex
    def __init__(self, data):
        self.data = data  # Node value
        self.next = None  # Node next pointer


class Solution:
    def solution_recursive(self, l1, l2):
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.solution_recursive(l1.next, l2)
        return l1

