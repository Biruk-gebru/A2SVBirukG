# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first_num, path):
            if len(path) == k:
                ans.append(path[:])
                return

            if first_num > n:
                return
            path.append(first_num)
            backtrack(first_num + 1, path)
            path.pop()
            backtrack(first_num + 1, path)


        ans = []
        backtrack(1, [])
        return ans

                