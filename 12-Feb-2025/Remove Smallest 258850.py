# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    leng = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    count = 0
    for i in range(leng-1):
        if nums[i+1] - nums[i] <= 1:
            count += 1
    if count == leng - 1:
        print("YES")
    else:
        print("NO")
