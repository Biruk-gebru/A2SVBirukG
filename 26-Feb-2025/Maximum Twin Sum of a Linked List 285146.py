# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        le = 0
        count = head
        while count:
            le += 1
            count = count.next
        slow = fast=head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
        node = None
        last_node = None
        reverse = slow
        while reverse:
            temp = reverse.next
            reverse.next = node
            node = reverse
            reverse = temp

            if not reverse:
                last_node = node
        sol = float('-inf')
        for _ in range(le):
            if head and last_node:
                print(sol)
                sol = max(sol, head.val + last_node.val)
                head = head.next
                last_node = last_node.next
        return sol



        