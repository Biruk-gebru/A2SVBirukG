# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

from typing import List  

class Solution:  
    def maximumProduct(self, nums: List[int]) -> int:   
        
        pos = [p for p in nums if p >= 0]  
        neg = [n for n in nums if n < 0]  
        
        pos.sort(reverse=True)  
        neg.sort()  

        max_product = float('-inf')  

        
        if len(pos) >= 3:  
            max_product = max(max_product, pos[0] * pos[1] * pos[2])  

        if len(neg) >= 2 and len(pos) > 0:  
            max_product = max(max_product, neg[0] * neg[1] * pos[0]) 

        if len(neg) >= 3 and len(pos) == 0:
             max_product = max(max_product, neg[-3] * neg[-2] * neg[-1])

        if len(neg) >= 3:  
            max_product = max(max_product, neg[0] * neg[1] * neg[2])  
        print(max_product)
        return max_product