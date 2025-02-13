# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set(map(int, input().split()))))
    if len(arr) == 1:
        print(arr[0])
    else:
        print(arr[-2])  