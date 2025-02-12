# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ca = Counter(arr1)
        sol = []
        for n in arr2:
            sol.extend([n]*ca[n])
        a1 = [p for p in arr1 if p not in arr2]
        a1.sort()
        sol.extend(a1)
        return sol
        