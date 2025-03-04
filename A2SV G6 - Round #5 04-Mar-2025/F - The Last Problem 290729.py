# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate the original sum S.
original_sum = sum(a[i] * b[i] for i in range(n))

best = 0  # Best improvement found by reversing a subarray

# Check odd-length reversals (centered at i)
for center in range(n):
    current_delta = 0
    l, r = center - 1, center + 1
    while l >= 0 and r < n:
        # Calculate the delta added by expanding to include a[l] and a[r]
        current_delta += a[l] * b[r] + a[r] * b[l] - a[l] * b[l] - a[r] * b[r]
        best = max(best, current_delta)
        l -= 1
        r += 1

# Check even-length reversals (center between i and i+1)
for center in range(n - 1):
    current_delta = 0
    l, r = center, center + 1
    while l >= 0 and r < n:
        current_delta += a[l] * b[r] + a[r] * b[l] - a[l] * b[l] - a[r] * b[r]
        best = max(best, current_delta)
        l -= 1
        r += 1

# Output the maximum sum achievable after at most one reversal
print(original_sum + best)