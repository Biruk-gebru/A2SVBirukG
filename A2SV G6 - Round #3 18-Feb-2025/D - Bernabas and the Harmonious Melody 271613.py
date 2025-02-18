# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def min_removals_for_palindrome(s):  
    n = len(s)  
    min_removals = float('inf')  
  
    for char in range(ord('a'), ord('z') + 1):  
        candidate = chr(char)  
        left, right = 0, n - 1  
        removals = 0  
        
        while left < right:  
            if s[left] == s[right]:  
                left += 1  
                right -= 1  
            elif s[left] == candidate:  
                removals += 1  
                left += 1  
            elif s[right] == candidate:  
                removals += 1  
                right -= 1  
            else:  
                removals = float('inf')    
                break  
        
        min_removals = min(min_removals, removals)  

    return min_removals if min_removals != float('inf') else -1  
  
t = int(input())  
for _ in range(t):  
    n = int(input())  
    s = input().strip()  
    result = min_removals_for_palindrome(s)  
    print(result)