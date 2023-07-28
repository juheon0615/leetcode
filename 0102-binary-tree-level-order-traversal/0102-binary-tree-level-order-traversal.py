# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        #bfs        
        q = [root]
        ret = []
        while q:
            nextQ = []
            level = []
            while q:
                node = q.pop(0)
                if node is None:
                    continue
                nextQ.append(node.left)
                nextQ.append(node.right)
                level.append(node.val)
            
            if level:
                ret.append(level)
            q = nextQ
        
        
        return ret
                
        
        