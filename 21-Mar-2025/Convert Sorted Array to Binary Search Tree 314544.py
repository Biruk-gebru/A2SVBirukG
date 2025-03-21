# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def dfs(left,right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node
    
        return dfs(0 , n - 1)
        


            
        
        