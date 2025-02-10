# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,low,mid,high):
            temp=[]
            i=low
            j=mid+1
            while i<=mid and j<=high:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=high:
                temp.append(nums[j])
                j+=1
            for k in range(low,high+1):
                nums[k]=temp[k-low]
        def ms(nums,low,high):
            if low==high:
                return
            mid=(low + high)//2
            ms(nums,low,mid)
            ms(nums,mid+1,high)
            merge(nums,low,mid,high)
        low=0
        high=len(nums)-1
        ms(nums,low,high)
        return nums


        