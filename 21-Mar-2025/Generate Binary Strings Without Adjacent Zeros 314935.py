# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:  
    def validStrings(self, n: int) -> List[str]:  
        self.ans = []  
        k = 2   

        def backtrack(prev: List[int]):  
            if len(prev) == n:  
                if is_valid(prev):  
                    self.ans.append(''.join(map(str, prev)))  
                return  
            
            for j in range(k):  
                prev.append(j)  
                backtrack(prev)  
                prev.pop()  
        
        def is_valid(subarray: List[int]) -> bool:  

            for i in range(len(subarray) - 1):  
                if subarray[i] == 0 and subarray[i + 1] == 0:  
                    return False  
            return True  

        backtrack([])  
        return self.ans 