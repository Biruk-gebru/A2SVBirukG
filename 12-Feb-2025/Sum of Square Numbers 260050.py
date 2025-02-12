# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(sqrt(c))
        while i <= j:
            if j == sqrt(c - i**2):
                return True
            if i **2 + j ** 2 > c:
                j -=1
            else:
                i += 1
        return False
        
        