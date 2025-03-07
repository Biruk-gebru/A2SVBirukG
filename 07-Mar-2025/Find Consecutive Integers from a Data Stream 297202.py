# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:  

    def __init__(self, value: int, k: int):  
        self.value = value  
        self.k = k  
        self.count = 0  
        self.stream = deque()  

    def consec(self, num: int) -> bool:  
        if len(self.stream) == self.k:  
            removed = self.stream.popleft()  
            if removed == self.value:  
                self.count -= 1 

        if num == self.value:  
            self.count += 1   

        self.stream.append(num)

        return self.count == self.k  