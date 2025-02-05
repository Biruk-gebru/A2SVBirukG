# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:  

    def __init__(self):  
        self.tracker = {}  
        self.arr = []      

    def insert(self, val: int) -> bool:  
        if val in self.tracker:  
            return False  
        self.tracker[val] = len(self.arr)  
        self.arr.append(val)  
        return True  

    def remove(self, val: int) -> bool:  
        if val not in self.tracker:  
            return False  

        index_to_remove = self.tracker[val]  
        last_element = self.arr[-1]  

        self.arr[index_to_remove] = last_element  
        self.tracker[last_element] = index_to_remove 

        
        self.arr.pop()  
        del self.tracker[val]  
        return True  

    def getRandom(self) -> int:  
        return random.choice(self.arr)  

# Example usage:  
# obj = RandomizedSet()  
# param_1 = obj.insert(val)  
# param_2 = obj.remove(val)  
# param_3 = obj.getRandom()  