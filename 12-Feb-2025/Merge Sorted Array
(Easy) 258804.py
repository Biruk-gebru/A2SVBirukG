# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = 0
        j = 0
        while i<m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                temp.append(nums2[j])
                j += 1
            else:
                temp.append(nums1[i])
                temp.append(nums2[j])
                i+= 1
                j += 1
        while i < m:
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1
        print(temp)
        for i in range(len(nums1)):
            nums1[i] = temp[i]
        