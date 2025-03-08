# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()
        size = 1
        l = 0
        for r in range(len(nums)):

            while mx and mx[-1] < nums[r]:
                mx.pop()

            mx.append(nums[r]) 

            while mn and mn[-1] > nums[r]:
                mn.pop()
                
            mn.append(nums[r])

            if mx[0] - mn[0] <= limit:
                size = max(size, r - l + 1)
            else:
                while mx and mn and mx[0] - mn[0] > limit:
                    if nums[l] == mx[0]: mx.popleft()
                    if nums[l] == mn[0]: mn.popleft()
                    l += 1
            
        return size
