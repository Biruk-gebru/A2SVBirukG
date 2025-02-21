# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ab = (int(a, 2))
        bb = (int(b, 2))
        sol = []
        f = False
        for n in str(bin(ab + bb)):
            if f:
                sol.append(n)
            if not f and n == "b":
                f = True
        return "".join(sol)
        