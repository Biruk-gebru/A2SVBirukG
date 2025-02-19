# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        sol = head
        while head:
            count += 1
            head = head.next
        count = (count // 2)  
        s = 0
        while  s <count:
            sol = sol.next
            s += 1
        return sol
        
        