# Problem: Running Miles - https://codeforces.com/problemset/problem/1826/D

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    lefta = []
    for i in range(n):
        lefta.append(a[i] + i)
    su = lefta[0]
    for i in range(n):
        su = max(su, lefta[i])
        lefta[i] = su
    righta = []
    for i in range(n):
        righta.append(a[i] - i)
    su = righta[n-1]
    for i in range(n-1, -1, -1):
        su = max(su, righta[i])
        righta[i] = su
    sol = float('-inf')
    for i in range(1,n-1):
        sol = max(sol,lefta[i-1] + righta[i+1] + a[i])
    print(sol)
    
                
            
    