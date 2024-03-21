A=set(map(int,input().split()))
n=int(input())
sol=True
for i in range(n):
    n1=set(map(int,input().split()))
    if len(A)>len(n1):
        if not all(num in A for num in n1):
            sol=False
print(sol)
