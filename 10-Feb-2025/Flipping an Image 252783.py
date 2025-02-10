# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        sol = []
        for im in image:
            temp = []
            for i in im:
                if i == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            sol.append(temp[::-1])
        return sol
        