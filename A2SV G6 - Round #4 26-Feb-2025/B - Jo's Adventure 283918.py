# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n , t = map(int,input().split())

arr = list(map(int,input().split()))
first_last = [0]
last_first = [0]
for i in range(n-1):
    if arr[i] > arr[i+1]:
        first_last.append(arr[i] - arr[i+ 1])
    else:
        first_last.append(0)
for i in range(n-1,0,-1):
    if arr[i] > arr[i-1]:
        last_first.append(arr[i] - arr[i - 1])
    else:
        last_first.append(0)
last_first.append(0)
last_first.reverse()
prevfl = []
su = 0 
for i in range(n):
    prevfl.append(first_last[i] + su)
    su += first_last[i]
prevlf = []
su = 0 
for i in range(n):
    prevlf.append(last_first[i] + su)
    su += last_first[i]
# prevlf.reverse()
for _ in range(t):
    l, r = map(int, input().split())
    if l < r:
        print(prevfl[r-1] - prevfl[l-1])
    else:
        print(prevlf[l-1]- prevlf[r-1])



    

