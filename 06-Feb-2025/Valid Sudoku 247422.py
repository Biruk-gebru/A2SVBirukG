# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setR = [set() for _ in range(9)]
        setC = [set() for _ in range(9)]
        setB = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                idx = (i // 3) * 3 + (j // 3)
                if (board[i][j] in setB[idx]) or (board[i][j] in setC[j]) or (board[i][j] in setR[i]):
                    return False
                setR[i].add(board[i][j])
                setC[j].add(board[i][j])
                setB[idx].add(board[i][j])

        return True
    