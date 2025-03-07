# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if len(logs[i])==3 and logs[i][0] == "." and stack:
                stack.pop()
            elif logs[i][0] != ".":
                stack.append(logs[i])
        return len(stack)
        