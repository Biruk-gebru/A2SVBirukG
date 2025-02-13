# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n , s = map(int, input().split())

nums = list(map(int, input().split()))
j = 0
su = 0
sol = 0
for i in range(n):
    su += nums[i]
    while su > s:
        su -= nums[j]
        j += 1
    sol = max(sol, i - j + 1)
print(sol)
