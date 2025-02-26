# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

t = int(input())
arr = list(map(int, input().split()))
su = 0
arr.sort()
print(arr[((t + 1) //2) - 1])