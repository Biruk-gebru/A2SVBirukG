# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [p for p in nums if p>=0]
        neg = [n for n in nums if n < 0]
        return list(chain(*zip(pos,neg)))
        