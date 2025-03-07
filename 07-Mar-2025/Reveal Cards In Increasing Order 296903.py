# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sol=deque()
        deck.sort()
        for i in range(len(deck)):
            if len(sol)>=2:
                sol.appendleft(sol[-1])
                sol.pop()
            sol.appendleft(deck.pop())
        return list(sol)

           