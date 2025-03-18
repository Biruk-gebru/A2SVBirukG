# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

class Solution:  
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:  
        # Return if the tree is empty  
        if not root:  
            return root  
        
        # Find the node to be deleted  
        if key < root.val:  
            root.left = self.deleteNode(root.left, key)  
        elif key > root.val:  
            root.right = self.deleteNode(root.right, key)  # Changed 'val' to 'key'  
        else:  
            # If the node is with only one child or no child  
            if not root.left:  
                return root.right  
            elif not root.right:  
                return root.left  
            
            # If the node has two children,  
            # place the inorder successor in position of the node to be deleted  
            temp = self.getMinValueNode(root.right)  # Find the inorder successor  
            root.val = temp.val  
            # Delete the inorder successor  
            root.right = self.deleteNode(root.right, temp.val)  

        return root  

    def getMinValueNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:  
        current = node  
        while current.left:  
            current = current.left  
        return current  