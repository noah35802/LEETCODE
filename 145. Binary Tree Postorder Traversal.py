# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def post(node):
            if not node:
                return
            post(node.left)
            post(node.right)
            res.append(node.val)
        post(root)
        return res
        
