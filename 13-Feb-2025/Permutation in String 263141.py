# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        s2c = Counter(s2[:len(s1) - 1])
        left = 0
        for right in range(len(s1) - 1, len(s2)):
            s2c[s2[right]] += 1
            if s2c == s1c:
                return True
            
            s2c[s2[left]] -= 1
            if s2c[s2[left]] == 0:
                s2c.pop(s2[left])
            
            left += 1

        return False
