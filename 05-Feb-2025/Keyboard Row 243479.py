# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {  
        'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9}  # Row 1: qwertyuiop  
        row2={'a': 10, 's': 11, 'd': 12, 'f': 13, 'g': 14, 'h': 15, 'j': 16, 'k': 17, 'l':18} # Row 2: asdfghjkl  
        row3={'z': 19, 'x': 20, 'c': 21, 'v': 22, 'b': 23, 'n': 24, 'm': 25}  # Row 3: zxcvbnm  
        sol = []
        for elem in words:
            flag = True
            if elem[0].lower() in row1:
                for el in elem:
                    if el.lower() not in row1:
                        flag = False
                        break
            elif elem[0].lower() in row2:
                for el in elem:
                    if el.lower() not in row2:
                        flag = False
                        break
            else:
                for el in elem:
                    if el.lower() not in row3:
                        flag = False
                        break
            if flag:
                sol.append(elem)
        return sol

        