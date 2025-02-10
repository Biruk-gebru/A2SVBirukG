# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))  

        str_nums.sort(key=lambda x: x * 10, reverse=True)  
         
        largest_num = ''.join(str_nums)  
        
        return largest_num if largest_num[0] != '0' else '0'  

        