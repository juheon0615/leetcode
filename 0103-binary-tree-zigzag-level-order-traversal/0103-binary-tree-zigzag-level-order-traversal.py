# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if len(ret) % 2 == 0:
                    ret.append(level)
                else:
                    ret.append(level[::-1])
            q = nextQ
        
        
        return ret