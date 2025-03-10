# Problem: Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:  
    def minInsertions(self, s: str) -> int:  
        stack = []  
        insertions = 0  
        i = 0  

        while i < len(s):  
            if s[i] == '(':  
                stack.append(s[i])  
            elif s[i] == ')':  
                if stack:  
                    stack.pop()  
                else:  
                    insertions += 1  
            
             
            if i + 1 < len(s) and s[i] == ')' and s[i + 1] == ')':  
                i += 1 
            else:  
                if s[i] == ')' and (i + 1 >= len(s) or s[i + 1] != ')'):   
                    insertions += 1  
                
            i += 1  

        
        return insertions + len(stack) * 2 
