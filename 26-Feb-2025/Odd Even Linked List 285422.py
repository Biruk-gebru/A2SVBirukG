# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        less_head = ListNode(0)  
        greater_head = ListNode(0)  
        less = less_head  
        greater = greater_head  
        
        temp = head 
        idx = 1 
        while temp:  
            if idx %2 != 0:  
                less.next = temp  
                less = less.next  
            else:  
                greater.next = temp  
                greater = greater.next 
            temp = temp.next 
            idx += 1 
        
        greater.next = None  
        less.next = greater_head.next  
        
        return less_head.next 