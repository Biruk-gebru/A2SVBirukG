# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        count1 = 0
        sumR = 0
        for b in range(len(boxes)):
            if boxes[b] == "1":
                sumR += b
                count1 += 1
        sol = []
        l = 0
        sumL = 0
        for b in boxes:
            sol.append(sumR + sumL)

            if b == "1":
                count1 -= 1
                l += 1

            sumL += l
            sumR -= count1

        return sol
        