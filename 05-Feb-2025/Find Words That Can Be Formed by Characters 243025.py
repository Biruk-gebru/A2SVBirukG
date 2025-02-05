# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sol = 0
        char_c = Counter(chars)
        for elem in words:
            elem_c = Counter(elem)
            flag = True
            for k,v in elem_c.items():
                if k in char_c and v <= char_c[k]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                sol += len(elem)
        return sol

                    

        