# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
    
        while temp:
            count += 1
            temp = temp.next
        if count - n == 0:
            head = head.next
            return head
        c = 0 
        prev = head
        while prev:
            c += 1
            if c == count - n :
                temp = prev
                post = prev.next.next
                prev.next = post
            else:
                prev = prev.next
        return head



        return temp
    
        