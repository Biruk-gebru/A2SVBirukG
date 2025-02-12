# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        d = Counter(changed)
        sol = []
        for elem in changed:
            if not d[elem]:
                continue
            d[elem] -= 1
            if not d[elem]:
                del d[elem]
                
            if elem * 2 in d:
                sol.append(elem)
                d[elem * 2] -= 1 
                if not d[elem * 2]:
                    del d[elem * 2]
            else:
                return []
            
            
        return sol 
        