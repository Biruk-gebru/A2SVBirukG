# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        s += "1"
        one = 0
        zero = 0
        left = 0
        sol = 0
        for right in range(len(s)):
            if s[right] == "1":
                while left < right:
                    if s[left]=="1":
                        one += 1
                    else:
                        zero += 1
                    left += 1
            sol += one* zero
            zero = 0
        return sol
            
                
            
            
        