# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sol = []
        for i in range(len(arr),1,-1):
            k = arr.index(i)
            sol.append(k+1)
            sol.append(i)
            arr = arr[0:k+1][::-1] + arr[k+1:]
            arr = arr[0:i][::-1] + arr[i:]
        return sol
        