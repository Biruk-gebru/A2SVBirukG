# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        

        stackp = []
        stackl = []
        for i in range(len(s)):
            if s[i] == "(":
                stackp.append(i)
                stackl.append("")
            elif s[i] == ")":
                start = stackp.pop()
                stackl.append("")
                reverse(stackl,start,i)
            else:
                stackl.append(s[i])
        

        return "".join(stackl)
        

                

        