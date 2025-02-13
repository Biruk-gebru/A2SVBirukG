# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        bi = 0
        for elem in a:
            if bi < len(b) and elem == b[bi]:
                bi += 1
        return bi == len(b)
   