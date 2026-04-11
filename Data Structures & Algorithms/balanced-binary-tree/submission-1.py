# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def get_max_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_max_height(root.left), self.get_max_height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        left = self.get_max_height(root.left)
        right = self.get_max_height(root.right)
        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        