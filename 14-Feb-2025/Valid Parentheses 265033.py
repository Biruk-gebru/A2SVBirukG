# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:  
    def isValid(self, s: str) -> bool:  
        stack = []  
        matching_brackets = {')': '(', '}': '{', ']': '['}  
        
        for element in s:  
            if element in matching_brackets.values():  
                stack.append(element)  
            elif element in matching_brackets.keys():  
                if stack and stack[-1] == matching_brackets[element]:  
                    stack.pop()  
                else:  
                    return False  
   
        return len(stack) == 0 