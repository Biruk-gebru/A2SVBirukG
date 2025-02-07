# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = [s for s in nums if s < pivot]
        equal = [e for e in nums if e == pivot]
        large = [l for l in nums if l>pivot]
        return small + equal + large
        