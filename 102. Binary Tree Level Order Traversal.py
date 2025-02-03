# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        q = deque()
        res = []
        q.append(root)
        
        while q:
            lenq = len(q)
            level = []
            
            for _ in range(lenq):
                node = q.popleft()
                level.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                    
                if node.right is not None:
                    q.append(node.right)
            
            res.append(level)
           
        return res
        
