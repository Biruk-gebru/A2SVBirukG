# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        stack = []
        for i in range(len(arr)):
            if arr[i] == 0:
                stack.append(i)
        for j in range(len(stack)):
            arr.insert(stack[j]+j, 0)
        while len(arr) > n:
            arr.pop()        