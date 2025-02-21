# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution:  
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:    
        length = 0  
        temp = head  
        while temp:  
            length += 1  
            temp = temp.next  

        curr = head  
        prev = None  
        next_node = None  
        mark = None  
        is_first_group = True  

        for _ in range(length // k):
            last = curr    
            prev = None  
            
            for _ in range(k):   
                next_node = curr.next  
                curr.next = prev  
                prev = curr  
                curr = next_node  

            if is_first_group:  
                head = prev  
                is_first_group = False  
            else:    
                mark.next = prev  

            mark = last    

        mark.next = curr  
        return head  