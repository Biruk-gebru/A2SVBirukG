# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:  
    def numTilePossibilities(self, tiles: str) -> int:  
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        self.sol = 0

        def backtracking(path,used):
            if path:
                self.sol += 1
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i-1] and not used[i - 1]:
                    continue
                used[i] = True
                backtracking(path + tiles[i], used)
                used[i] = False
                
        backtracking("",used)
        return self.sol