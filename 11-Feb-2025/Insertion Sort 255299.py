# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # for i in range(1,len(arr)):
    j=n-1
    while arr[j-1]>arr[j]:
        temp=arr[j]
        arr[j]=arr[j-1]
        for num in arr:
            print(num,end=' ')
        print()
        arr[j-1],arr[j]=temp,arr[j-1]
        j-=1
        if j==0:
            break
    for num in arr:
        print(num, end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
