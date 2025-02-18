# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t = int(input())

for _ in range(t):
    n , x = map(int, input().split())
    row = sorted(list(map(int, input().split())))

    flag = True
    for i in range(n):
        j = i + n
        if abs(row[i] - row[j]) >= x:
            j -= 1
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

