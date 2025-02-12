# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

op = input()
op = list(op)
newA = []
for n in op:
    if n == "+":
        continue 
    newA.append(n)
newA.sort()
sol = []
for i in range(len(newA)):
    sol.append(newA[i])
    sol.append("+")
sol.pop()
print("".join(sol))