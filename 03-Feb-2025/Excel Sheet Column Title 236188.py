# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        rem = []
        while columnNumber > 0:
            columnNumber -= 1
            rem.append(columnNumber % 26)
            columnNumber //= 26
            print(columnNumber)
        sol = ""
        for r in rem:
            sol += chr(ord("A") + r)
        return sol[::-1]  
        
        