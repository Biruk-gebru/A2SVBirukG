# Problem: Partition List - https://leetcode.com/problems/partition-list/

class Solution:  
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:  
        less_head = ListNode(0)  
        greater_head = ListNode(0)  
        less = less_head  
        greater = greater_head  
        
        temp = head  
        while temp:  
            if temp.val < x:  
                less.next = temp  
                less = less.next  
            else:  
                greater.next = temp  
                greater = greater.next 
            temp = temp.next  
        
        greater.next = None  
        less.next = greater_head.next  
        
        return less_head.next 