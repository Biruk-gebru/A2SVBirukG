# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

  
class Solution:  
    def __init__(self):  
        self.sol = []  

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        if not root:  
            return []  

        current_level = [root]  
        left_to_right = True  

        while current_level:  
            level_values = []  
            next_level = []  

            for node in current_level:  
                level_values.append(node.val)  
                if node.left:  
                    next_level.append(node.left)  
                if node.right:  
                    next_level.append(node.right)  

            if not left_to_right:  
                level_values.reverse()  

            self.sol.append(level_values)  
            current_level = next_level  
            left_to_right = not left_to_right  

        return self.sol  