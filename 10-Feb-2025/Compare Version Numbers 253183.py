# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) > len(v2):
            for _ in range(len(v1) - len(v2) ):
                v2.append("0")
        if len(v1) < len(v2):
            for _ in range(len(v2) - len(v1) ):
                v1.append("0")
        p = 0
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                p = 1
                return 1
            elif int(v1[i]) < int(v2[i]):
                p = 2
                return -1
        return 0
        
        
        