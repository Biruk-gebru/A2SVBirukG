# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = map(int, input().split())

arr = (list(map(int, input().split())))

counter = 0
curr = 0
left = 0
for i in range(n):
    curr += arr[i]
    while left < n and curr > t:
        curr -= arr[left]
        left += 1
    counter = max(counter, i - left + 1) 
print(counter)