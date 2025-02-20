# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        dummy = ListNode(0) 
        dummy.next = head  
        current = dummy  
        
        while current.next:  
            if current.next.next and current.next.val == current.next.next.val:  
                duplicate_val = current.next.val  
                if current.next and current.next.val == duplicate_val:  
                    current.next = current.next.next  
            else:  
                current = current.next 
        
        return dummy.next  