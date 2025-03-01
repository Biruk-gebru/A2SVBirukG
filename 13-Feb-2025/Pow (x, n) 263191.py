# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def po(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n < 0:
                return 1 / po(x, -n)
            if n % 2 == 0:
                return po(x * x, n // 2)
            else:
                return x * po(x, n - 1)

        return po(x, n)

        