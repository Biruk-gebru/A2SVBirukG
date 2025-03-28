# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ls = list(c.items())
        ls.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in ls[:k]]