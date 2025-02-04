# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:  
    def removeComments(self, source: List[str]) -> List[str]:  
        sol = [] 
        flag = True  
        temp = ""  

        for line in source:  
            e = 0 
            while e < len(line):  
                if flag: 
                    if e < len(line) - 1 and line[e] == "/" and line[e + 1] == "/":  
                        break  
                    elif e < len(line) - 1 and line[e] == "/" and line[e + 1] == "*":  
                        flag = False  
                        e += 1  
                    else:  
                        temp += line[e] 
                else: 
                    if e < len(line) - 1 and line[e] == "*" and line[e + 1] == "/":  
                        flag = True  
                        e += 1 
                
                e += 1  
            
            if temp and flag:  
                sol.append(temp) 
                temp = "" 
            
        return sol