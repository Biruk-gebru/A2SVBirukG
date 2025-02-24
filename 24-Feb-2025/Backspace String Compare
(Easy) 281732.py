# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []
        for elem in s:
            if sstack and elem == "#":
                sstack.pop()
            elif elem != "#":
                sstack.append(elem)
        for telem in t:
            if tstack and telem == "#":
                tstack.pop()
            elif telem != "#":
                tstack.append(telem)
        print(tstack, sstack)
        return tstack == sstack
        