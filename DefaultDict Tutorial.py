mn=list(map(int,input().split()))
m1=mn[0]
n1=mn[1]
m=[]
n=[]
for i in range(m1):
    m.append(input())
for j in range(n1):
    n.append(input())
for r in range(n1):
    c=n[r]
    sol=[]
    for k in range(m1):
        if c==m[k]:
            sol.append(k+1)
    if len(sol)!=0:
        print(*sol)
    else:print(-1)
