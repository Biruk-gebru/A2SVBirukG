# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())  
a = list(map(int, input().split()))  
m = int(input())  
b = list(map(int, input().split()))  

if sum(a) != sum(b):
    print(-1)
else:
    sa = [a[0]]
    for i in range(1,n):
        sa.append(sa[-1] + a[i])
    sb = [b[0]]
    for i in range(1,m):
        sb.append(sb[-1] + b[i])
    ida = idb = 0
    sol = 0
    while ida < n and idb < m:
        if sa[ida] == sb[idb]:
            sol += 1
            ida += 1
            idb += 1
        elif sa[ida] < sb[idb]:
            ida += 1
        else:
            idb += 1
    print(sol)
