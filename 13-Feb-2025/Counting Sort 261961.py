# Problem: Counting Sort - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    na=[0]*100
    iw=0
    while iw<100:
        for num in arr:
            if num==iw:
                na[iw]+=1
        iw+=1
    return na