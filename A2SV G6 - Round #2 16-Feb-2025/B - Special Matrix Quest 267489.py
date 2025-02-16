# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

t = int(input())
matrix = []
for _ in range(t):
    n = list(map(int, input().split()))
    matrix.append(n)

if t == 1:
    print(matrix[0][0])
else:
    idxCi = (t - 1)//2
    idxCj = (t-1)//2
    sumDM = 0
    sumCC = 0
    sumCR = 0
    sumDS = 0
    for i in range(t):
        for j in range(t):
            if i == j:
                sumDM += matrix[i][j]
            if j == (t -1)/2:
                sumCC += matrix[i][j]
            if i == (t - 1)/2:
                sumCR += matrix[i][j]
            if i + j == t - 1:
                sumDS += matrix[i][j]
    # print(sumCC , sumCR , sumDM , sumDS , sumC)
    print(sumCC + sumCR + sumDM + sumDS - (matrix[idxCi][idxCj])*3)
    
