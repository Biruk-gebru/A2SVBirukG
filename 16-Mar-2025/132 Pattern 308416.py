# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cur_min = nums[0]
        stack = [[cur_min, cur_min]]
        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack and nums[i] >  stack[-1][1]:
                return True
            stack.append([nums[i], cur_min])
            cur_min = min(cur_min, nums[i])
        return False


        
        