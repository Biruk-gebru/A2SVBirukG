# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        c = sorted(c.items(),key = lambda x: x[1], reverse = True)
        sol = 0
        curr = len(arr)
        for k in c:
            sol += 1
            curr -= k[1]
            if curr <= len(arr)//2:
                break
        return sol


        