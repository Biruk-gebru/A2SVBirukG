# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        def backtrack(s: str):   
            if len(s) == 2 * n:  
                if self.is_valid(s):   
                    result.append(s)  
                return  
            
           
            for _ in range(2):  
                if len(s) < 2 * n:  
                    if _ == 0 and s.count('(') < n: 
                        backtrack(s + '(')  
                    elif _ == 1 and s.count(')') < s.count('('):  
                        backtrack(s + ')')  
            
        result = []  
        backtrack('')  
        return result  
    
    def is_valid(self, s: str) -> bool:  
        balance = 0  
        for char in s:  
            if char == '(':  
                balance += 1  
            else:  
                balance -= 1  
            if balance < 0:  
                return False  
        return balance == 0
        
        