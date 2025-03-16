# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:  
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:  
        if not root:  
            return []  

        sol = []  
        queue = deque([root])  

        while queue:  
            level_size = len(queue)  
            max_value = float('-inf')  

            for _ in range(level_size):  
                node = queue.popleft()  
                max_value = max(max_value, node.val)  

                
                if node.left:  
                    queue.append(node.left)  
                if node.right:  
                    queue.append(node.right)  

            sol.append(max_value)  

        return sol  