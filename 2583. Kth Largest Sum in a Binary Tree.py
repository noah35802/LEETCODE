class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res=[]
        q=deque([root])
        while q:
            n=len(q)
            level_sum=0
    
            for i in range(n):
                node=q.popleft()
                level_sum+=node.val
    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum)
        if k>len(res):
            return -1
        res.sort(reverse=True)
        return res[k-1]
