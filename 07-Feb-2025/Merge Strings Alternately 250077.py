# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        sol=""
        while i<len(word1) and j<len(word2):
            sol+=word1[i]
            i+=1
            sol+=word2[j]
            j+=1
        sol+=word1[i:]
        sol+=word2[j:]
        return sol

        