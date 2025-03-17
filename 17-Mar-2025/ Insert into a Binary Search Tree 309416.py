# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)  
        def ins(node, val):
            if node is None:
                return TreeNode(val)  
            if val > node.val:
                node.right = ins(node.right, val) 
            else:
                node.left = ins(node.left, val) 
            return node  
        
        return ins(root, val)

        