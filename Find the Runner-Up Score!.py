n = int(input())
arr = map(int, input().split())
arr=sorted(arr,reverse=True)
maxx=arr[0]
for i in range(n):
    if arr[i]!=maxx:
        maxx=arr[i]
        break
print(maxx)
