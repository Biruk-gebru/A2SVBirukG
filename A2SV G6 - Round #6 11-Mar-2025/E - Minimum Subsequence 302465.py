# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

def solve():  
    n = int(input())  
    s = input()  
    
    zeros = []  
    ones = []   
    
    result = [0] * n  
    num_subsequences = 0  
    
    for i in range(n):  
        if s[i] == '0':  
            if ones:  
                subsequence_index = ones.pop()  
                zeros.append(subsequence_index)  
                result[i] = subsequence_index  
            else:  
                num_subsequences += 1  
                zeros.append(num_subsequences)  
                result[i] = num_subsequences  
        else: 
            if zeros:  
                subsequence_index = zeros.pop()  
                ones.append(subsequence_index)  
                result[i] = subsequence_index  
            else:  
                num_subsequences += 1  
                ones.append(num_subsequences)  
                result[i] = num_subsequences  
                
    print(num_subsequences)  
    print(*result)  

t = int(input())  
for _ in range(t):  
    solve()  