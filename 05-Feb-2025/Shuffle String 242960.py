# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={}
        for i in range(len(s)):
            dic[indices[i]]=s[i]
        s=sorted(dic.items())
        print(s)
        ss=''
        for i in  range(len(s)):
            ss+=s[i][1]
        return ss