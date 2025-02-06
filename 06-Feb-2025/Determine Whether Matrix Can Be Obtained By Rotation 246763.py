# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        temp = [[0] * len(mat) for _ in range(len(mat[0]))]
        for i in range(len(mat)):
                for j in range(len(mat[i])):
                    temp[i][j] = mat[j][i]
        for i in range(len(temp)):
            temp[i]= temp[i][::-1]
        print(temp)
        if temp == target:
            return True
        for _ in range(2):
            tp = temp
            temp = [[0] * len(mat) for _ in range(len(mat[0]))]
            for i in range(len(tp)):
                for j in range(len(tp[i])):
                    temp[i][j] = tp[j][i]
            for i in range(len(temp)):
                temp[i]= temp[i][::-1]
            print(temp)
            if temp == target:
                return True
        return False

        
        