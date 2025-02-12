# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j = 0, len(skill) - 1
        curr = skill[j] + skill[i]
        prod = 0
        while i<j:
            if skill[i] + skill[j] != curr:
                return -1
            prod += skill[i] * skill[j]
            i+=1
            j-=1
        return prod

        
        