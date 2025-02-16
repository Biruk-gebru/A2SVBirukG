# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())  
results = []  

for _ in range(t):  
    n = int(input())  
    grid = [input().strip() for _ in range(n)]  

    visited = set()  
    flips = 0  

    for i in range(n):  
        for j in range(n):  
            if (i, j) in visited:  
                continue  
        
            positions = [  
                (i, j),                   
                (j, n - 1 - i),          
                (n - 1 - i, n - 1 - j),  
                (n - 1 - j, i)           
            ]  
            
            values = [grid[x][y] for x, y in positions]  
            count_0 = values.count('0')  
            count_1 = values.count('1')  
            
            flips += min(count_0, count_1)  
            
            for pos in positions:  
                visited.add(pos)  

    print(flips)  
