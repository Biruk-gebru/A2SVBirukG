# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:  
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  
        if not matrix or not matrix[0]:  
            return []  
        
        sol = []  
        up, down = 0, len(matrix) - 1  
        left, right = 0, len(matrix[0]) - 1  
        
        while up <= down and left <= right:  
            # Traverse from left to right along the top row  
            for i in range(left, right + 1):  
                sol.append(matrix[up][i])  
            up += 1  
            
            # Traverse from top to bottom along the right column  
            for i in range(up, down + 1):  
                sol.append(matrix[i][right])  
            right -= 1  
            
            if up <= down:  # Make sure there's a bottom row left to traverse  
                # Traverse from right to left along the bottom row  
                for i in range(right, left - 1, -1):  
                    sol.append(matrix[down][i])  
                down -= 1  
            
            if left <= right:  # Make sure there's a left column left to traverse  
                # Traverse from bottom to top along the left column  
                for i in range(down, up - 1, -1):  
                    sol.append(matrix[i][left])  
                left += 1  
        
        return sol