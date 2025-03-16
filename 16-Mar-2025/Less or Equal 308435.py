# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

nk=list(map(int,input().split()))
nums=list(map(int,input().split()))
x=nk[0]
k=nk[1]
nums=sorted(nums)
n=0
counter=0
i=0
ind=0
while i<x:
    if nums[i]<=n:
        counter+=1
        i+=1
    else: 
        n+=1

    if counter==k:
        ind=i
        break
for j in range(ind,len(nums)):
    if nums[j]<=n:
        n=-1
        break
print (n)