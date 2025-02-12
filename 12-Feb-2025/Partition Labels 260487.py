# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {s[i]: i for i in range(len(s))}
        sol = []
        curr = 0
        j =0
        for i in range(len(s)):
            curr = max(curr, d[s[i]])
            if curr == i:
                sol.append(j + 1)
                j = 0
            else:
                j += 1
        return sol

        