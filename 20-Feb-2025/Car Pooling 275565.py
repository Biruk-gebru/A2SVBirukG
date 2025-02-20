# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for count, start, end in trips:
            events.append((start, count))   
            events.append((end, -count))   
        events.sort()
        current_passengers = 0
        for time, passenger_change in events:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
        return True