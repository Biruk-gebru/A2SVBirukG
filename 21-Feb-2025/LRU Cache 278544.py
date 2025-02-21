# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:  
    def __init__(self, capacity: int):  
        self.cache = OrderedDict()  
        self.capacity = capacity  

    def get(self, key: int) -> int:  
        if key not in self.cache:  
            return -1  
        else:  
            self.cache.move_to_end(key)  
            return self.cache[key]  
        
    def put(self, key: int, value: int) -> None:  
        if key in self.cache:  
            self.cache.move_to_end(key)  
        self.cache[key] = value  
        if len(self.cache) > self.capacity:  
            self.cache.popitem(last=False)  

# Example usage:  
# obj = LRUCache(capacity)  
# param_1 = obj.get(key)  
# obj.put(key, value)