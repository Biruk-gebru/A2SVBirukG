# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            f = n //2
            r = n - f
        else:
            f = n //2 + 1
            r = n - f
        return (pow(5,f, (10**9 + 7)) * pow(4,r, 10**9 + 7)) % (10**9 + 7)




        