# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sol=[]
        s=0
        m=n
        while m<len(nums) and s<n:
            sol.append(nums[s])
            sol.append(nums[m])
            s+=1
            m+=1
        return sol

        