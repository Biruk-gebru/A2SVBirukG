# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1 = s.count("1")
        c2 = s.count("0")
        sol = []
        if c1 > 0:
            sol.append("1")
            c1 -= 1
        while c2 > 0:
            sol.append("0")
            c2 -= 1
        while c1 > 0:
            sol.append("1")
            c1 -= 1
        return "".join(sol[::-1])
        

       


        