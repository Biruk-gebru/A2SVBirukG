# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sol = set()
        for elem in nums:
            temp = str(elem)
            sol.add(elem)
            sol.add(int(temp[::-1]))
        return len(sol)
                
        