# Problem: Array Manipulation - https://www.hackerrank.com/challenges/crush/problem

def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    for k in range(len(queries)):
        arr [queries[k][0]-1] += queries[k][2]
        if queries[k][1] < n:
            arr[queries[k][1]] -= queries[k][2]
    sol = arr[0]
    temp = 0
    for i in range(n):
        temp += arr[i]
        sol = max(sol,temp)
        
        
    return sol
