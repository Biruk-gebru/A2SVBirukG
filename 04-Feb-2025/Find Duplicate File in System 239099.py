# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_r = defaultdict(list)
        for elem in paths:
            temp = elem.split()
            for k in range(1,len(temp)):
                idxS= temp[k].index("(")
                dict_r[temp[k][idxS+1 : -1]].append(temp[0] + "/" + temp[k][:idxS])
        sol = []
        print(dict_r)
        for k,v in dict_r.items():
            if len(v) > 1:
                sol.append(v)
        return sol



        