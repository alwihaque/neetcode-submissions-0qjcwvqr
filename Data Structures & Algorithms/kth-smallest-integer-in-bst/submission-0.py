# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def dfs(root, k):
            if not root:
                return
            
            dfs(root.left, k)
            res.append(root)
            dfs(root.right, k)
        
        dfs(root, k)
        

        return res[k - 1].val
        