# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        temp = nums[-1 * k :] + nums[0: -1*k]
        for i in range(len(temp)):
            nums[i] = temp[i]
        