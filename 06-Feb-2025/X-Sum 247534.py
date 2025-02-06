# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())  

for _ in range(t):  
    board = []  
    m, n = map(int, input().split())  
    for _ in range(m):  
        row = list(map(int, input().split()))  
        board.append(row)  
    
    max_sum = float('-inf')  
    
    for i in range(m):  
        for k in range(n):  
            temp = board[i][k]  
            
            j, iin = k - 1, i - 1  
            while iin >= 0 and j >= 0:  
                temp += board[iin][j]  
                iin -= 1  
                j -= 1  
            
            j, iin = k + 1, i + 1  
            while iin < m and j < n:   
                temp += board[iin][j]  
                iin += 1  
                j += 1  
            
            j, iin = k - 1, i + 1  
            while iin < m and j >= 0:  
                temp += board[iin][j]  
                iin += 1  
                j -= 1  
            
            j, iin = k + 1, i - 1  
            while iin >= 0 and j < n:  
                temp += board[iin][j]  
                iin -= 1  
                j += 1  
            
            max_sum = max(max_sum, temp)  
    
    print(max_sum)