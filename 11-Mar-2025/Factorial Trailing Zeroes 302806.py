# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def factorial(self, n):
            if n <= 1:
                return 1
            return n * self.factorial(n-1)

    def trailingZeroes(self, n: int) -> int:
        f = factorial(n)
        sol = 0
        while f%10 == 0:
            sol += 1
            f //=10
        return sol

        
        