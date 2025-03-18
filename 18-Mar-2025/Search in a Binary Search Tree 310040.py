# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root 
            
        if root.val < val:   
            return self.searchBST(root.right,val)
        elif root.val> val:
            return self.searchBST(root.left,val)