# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        sol=[]
        ss=''
        for i in range(len(s)):
            if s[i]!=' ':
                ss+=s[i]
            else:
                sol.append(ss)
                ss=''
        if ss:
            sol.append(ss)
        i=1
        f=''
        while len(sol)>0:
            for r in range(len(sol)):
                if int(sol[r][-1])==i:  
                    l=len(sol[r])  
                    f+=sol[r][0:l-1] + ' ' 
                    i+=1
                    sol.remove(sol[r])
                    break  

        print(sol)
        return f.strip()  


            

        