# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if (n%2 != 0 and n%3!= 0 and n%5 != 0) or n<=0:
            return False
        while n > 1:
            print(n)
            if n%2 == 0:
                n //= 2
            elif n % 3 == 0:
                n//=3
            elif n%5 == 0:
                n //=5
            else:
                return False
        return True


            

        