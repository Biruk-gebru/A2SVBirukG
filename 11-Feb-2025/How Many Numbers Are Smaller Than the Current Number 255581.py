# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        sorted_nums = sorted(dic.keys())
        cumulative_count = {}
        cumulative_sum = 0
        for num in sorted_nums:
            cumulative_count[num] = cumulative_sum
            cumulative_sum += dic[num]
        result = []
        for n in nums:
            result.append(cumulative_count[n])
        
        return result
