# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:  

    def predictTheWinner(self, nums: List[int]) -> bool:  
        left , right = 0 , len(nums) -1
        @cache
        def sol(left, right):
            if left > right:
                return 0
            

            start = nums[left] + min(sol(left + 2, right), sol(left + 1, right - 1))
            end = nums[right] + min(sol(left ,right - 2), sol(left + 1, right - 1))
            return max(start, end) 

        return sol(left, right) >= (sum(nums)/2)
    