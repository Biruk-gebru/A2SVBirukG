# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict  

t = int(input())  
for _ in range(t):  
    n = int(input())  
    s = list(input())  
    
    sc = Counter(s)  
    
    leftD = 0  
    rightD = len(sc)  
    leftC = defaultdict(int)  
    max_value = 0  
    
    
    for i in range(n - 1):  
        char = s[i]  
        
        
        if leftC[char] == 0:  
            leftD += 1  
        leftC[char] += 1  
        
        if sc[char] == 1:  
            rightD -= 1  
        sc[char] -= 1  

        current_value = leftD + rightD  
        max_value = max(max_value, current_value)  
    
    print(max_value)