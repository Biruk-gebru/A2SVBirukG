# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            capacity, cur_days = 0, 1

            for weight in weights:
                if capacity + weight > mid:
                    cur_days += 1
                    capacity = 0

                capacity += weight

            if cur_days > days:
                left = mid + 1
            else:
                right = mid

        return left
            