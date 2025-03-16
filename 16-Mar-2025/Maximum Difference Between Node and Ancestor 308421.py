# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

class Solution:  
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:  
        def solve(node, current_min, current_max):  
            if not node:  
                return current_max - current_min  
            
            current_min = min(current_min, node.val)  
            current_max = max(current_max, node.val)  
            
            left_diff = solve(node.left, current_min, current_max)  
            right_diff = solve(node.right, current_min, current_max)  
            
            return max(left_diff, right_diff)  
        
        if not root:  
            return 0  
        
        return solve(root, root.val, root.val)  