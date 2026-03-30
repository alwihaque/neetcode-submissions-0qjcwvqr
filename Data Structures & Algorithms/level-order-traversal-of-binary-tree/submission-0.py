# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        while queue:
            queue_len = len(queue)
            level = []
            for i in range(queue_len):
                elem = queue.popleft()
                level.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            res.append(level)
        return res
            
            

        