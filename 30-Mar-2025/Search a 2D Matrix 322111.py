# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        ina = 0
        la = r * c - 1

        while ina <= la:
            mid = (ina + la) // 2
            ir = mid // c
            ic = mid % c
            num = matrix[ir][ic]
            if target == num:
                return(True)
                break
            elif target > num:
                ina = mid + 1
            else:
                la = mid - 1
        return(False)
        