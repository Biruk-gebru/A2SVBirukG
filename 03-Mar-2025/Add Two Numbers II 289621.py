# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
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
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        head1=l1
        a=""
        i=0
        while head1 is not None:
            a+=str(head1.val)
            i+=1
            head1=head1.next
        an=int(a)
        head2=l2
        b=""
        j=0
        while head2 is not None:
            b+=str(head2.val)
            head2=head2.next
            j+=1
        bn=int(b)
        c = an + bn
        value=str(c)[::-1]
        def create_linked_list(values):
            dummy_node = ListNode(0)
            current_node = dummy_node
            for value in values:
                current_node.next = ListNode(int(value))
                current_node = current_node.next
            return dummy_node.next

        return reverse(create_linked_list(value))
        
        