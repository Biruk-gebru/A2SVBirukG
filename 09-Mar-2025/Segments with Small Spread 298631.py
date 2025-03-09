# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque  

def solve():  
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))  

    count = 0  
    mn_deque = deque()  
    mx_deque = deque()  
    left = 0  

    for right in range(n):  
        while mn_deque and a[mn_deque[-1]] >= a[right]:  
            mn_deque.pop()  
        mn_deque.append(right)  

        while mx_deque and a[mx_deque[-1]] <= a[right]:  
            mx_deque.pop()  
        mx_deque.append(right)  


        while mx_deque and mn_deque and a[mx_deque[0]] - a[mn_deque[0]] > k:  
            left += 1  
            if mn_deque[0] < left:  
                mn_deque.popleft()  
            if mx_deque[0] < left:  
                mx_deque.popleft()  

        count += (right - left + 1)  

    print(count)  

solve()  