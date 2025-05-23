# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:  

    def __init__(self, k: int):  
        self.deque = deque()  
        self.capacity = k  
        self.size = 0  

    def insertFront(self, value: int) -> bool:  
        if self.isFull():  
            return False  
        self.deque.appendleft(value)  
        self.size += 1  
        return True  

    def insertLast(self, value: int) -> bool:  
        if self.isFull():  
            return False  
        self.deque.append(value)  
        self.size += 1  
        return True  

    def deleteFront(self) -> bool:  
        if self.isEmpty():  
            return False  
        self.deque.popleft()  
        self.size -= 1  
        return True  

    def deleteLast(self) -> bool:  
        if self.isEmpty():  
            return False  
        self.deque.pop()  
        self.size -= 1  
        return True  

    def getFront(self) -> int:  
        if self.isEmpty():  
            return -1  
        return self.deque[0]  

    def getRear(self) -> int:  
        if self.isEmpty():  
            return -1  
        return self.deque[-1]  

    def isEmpty(self) -> bool:  
        return self.size == 0  

    def isFull(self) -> bool:  
        return self.size == self.capacity  