# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        s = s.lstrip()
        arr = s.split(" ")
        arr.reverse()
        
        sol = []
        for a in arr:
            if a != '':
                sol.append(a)
        print(sol)

        return " ".join(sol)
        