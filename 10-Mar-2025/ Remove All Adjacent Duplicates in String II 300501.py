# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:  
    def removeDuplicates(self, s: str, k: int) -> str:  
        stack = []  
        
        for char in s:  
            if stack and stack[-1][0] == char:  
                stack[-1][1] += 1  
            else:  
                stack.append([char, 1])  
                
            if stack and stack[-1][1] == k:  
                stack.pop()  
    
        result = ''.join(char * count for char, count in stack)  
        
        return result  