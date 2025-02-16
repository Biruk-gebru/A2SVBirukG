# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def in_bounds(x, y, n, m):  
    return 0 <= x < n and 0 <= y < m  

def count_bombs(mine, x, y, n, m):  
    directions = [(-1, -1), (-1, 0), (-1, 1),   
                  (0, -1),          (0, 1),   
                  (1, -1), (1, 0), (1, 1)]  
    
    bomb_count = 0  
    for dx, dy in directions:  
        if in_bounds(x + dx, y + dy, n, m) and mine[x + dx][y + dy] == '*':  
            bomb_count += 1  
            
    return bomb_count  

def validate_minesweeper_field(n, m, mine):  
    for i in range(n):  
        for j in range(m):  
            if mine[i][j].isdigit():  
                expected_bombs = int(mine[i][j])  
                actual_bombs = count_bombs(mine, i, j, n, m)  
                if expected_bombs != actual_bombs:  
                    return "NO"  
            elif mine[i][j] == '.':  
                if count_bombs(mine, i, j, n, m) > 0:  
                    return "NO"  
    return "YES"  
 
n, m = map(int, input().split())  
mine = [input().strip() for _ in range(n)]  

result = validate_minesweeper_field(n, m, mine)  
print(result)