# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i][-1].isdigit():
                stack.append(int(operations[i]))
            elif operations[i] == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(stack[-1]*2)
        return sum(stack)

        