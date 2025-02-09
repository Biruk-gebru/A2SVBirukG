# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        sol = 0
        for k,v in c.items():
            size = k + 1
            o = math.ceil(v / size)
            sol += o * size
        return sol

        