# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())  
a = list(map(int, input().split()))  

m = int(input())  

pref = [0] * n  
pref[0] = a[0]  
for i in range(1, n):  
    pref[i] = pref[i - 1] + a[i]  

a.sort()  

modified_a = [0] * n  
modified_a[0] = a[0]  
for i in range(1, n):  
    modified_a[i] = modified_a[i - 1] + a[i]  

for _ in range(m):  
    t, l, r = map(int, input().split())  
    if t == 1:  
        print(pref[r - 1] - (pref[l - 2] if l > 1 else 0))  
    else:  
        print(modified_a[r - 1] - (modified_a[l - 2] if l > 1 else 0))  