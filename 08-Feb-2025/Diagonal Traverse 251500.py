# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sol = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp =sol[i+j]
                temp.append(mat[i][j])
                sol[i+j] = temp
        fmat = []
        print(sol)
        for k,v in sol.items():
            if k % 2 == 0:
                fmat.extend(v[::-1])
            else:
                fmat.extend(v)
        return fmat

        