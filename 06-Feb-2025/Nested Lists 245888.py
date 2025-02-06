# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    scores = list(set(sorted(scores)))
    if len(scores) < 2:
        x = scores[0]
    else:
        x = scores[1]
    records.sort(key = lambda x : x[1])
    pNames = []
    for i in range(len(records)-1,-1,-1):
        if records[i][1] == x:
            pNames.append(records[i][0])
    pNames.sort()
    for p in pNames:
        print(p)