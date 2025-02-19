# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = None

#         while head:
#             temp = head.next
#             head.next = node
#             node = head
#             head = temp
        
#         return node
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        last_node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

            if not head:
                last_node = node

        return last_node
        