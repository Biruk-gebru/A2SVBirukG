# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:  
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:  
        sol = [0] * (len(s) + 1)   
        for k in range(len(shifts)):  
            direction = shifts[k][2]   
            sol[shifts[k][0]] += 1 if direction == 1 else -1  
            if shifts[k][1] + 1 < len(sol):  
                sol[shifts[k][1] + 1] -= 1 if direction == 1 else -1  
  
        for j in range(1, len(sol)):  
            sol[j] += sol[j-1]  
         
        result = []  
        for i in range(len(s)):  
            new_char_index = (ord(s[i]) - ord('a') + sol[i]) % 26    
            result.append(chr(ord('a') + new_char_index))  
        
        return "".join(result)  
