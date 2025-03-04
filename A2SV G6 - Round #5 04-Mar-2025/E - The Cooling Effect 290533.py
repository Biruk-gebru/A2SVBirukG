# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

import sys  

input = sys.stdin.read  
data = input().strip().split('\n')  

# Read the number of test cases  
t = int(data[0])  
idx = 1  

results = []  

for _ in range(t):  
    # Skip empty lines if encountered  
    while idx < len(data) and data[idx] == '':  
        idx += 1  

    # Read n and k  
    n, k = map(int, data[idx].split())  
    idx += 1  
    
    # Read positions of air conditioners  
    pos = list(map(int, data[idx].split()))  
    idx += 1  
    
    # Read temperatures of air conditioners  
    temp = list(map(int, data[idx].split()))  
    idx += 1  

    # Initialize the temperature array  
    all = [float('inf')] * n  

    # Fill in the positions with their temperatures  
    for i in range(k):  
        all[pos[i] - 1] = temp[i]  

    # Forward pass to calculate minimum temperatures  
    forward = [float('inf')] * n  
    for i in range(n):  
        if i == 0:  
            forward[i] = all[i]  
        else:  
            forward[i] = min(forward[i - 1] + 1, all[i])  

    # Backward pass to calculate minimum temperatures  
    backward = [float('inf')] * n  
    for i in range(n - 1, -1, -1):  
        if i == n - 1:  
            backward[i] = all[i]  
        else:  
            backward[i] = min(backward[i + 1] + 1, all[i])  

    # Combine results from both passes  
    result = [min(forward[i], backward[i]) for i in range(n)]  
    results.append(" ".join(map(str, result)))  

# Print all results for each test case  
print("\n".join(results))  