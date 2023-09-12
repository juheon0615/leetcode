# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        q = [[root, None, None]]
        ret = math.inf
        
        while q:
            nextQ = []
            while q:
                node, left, right = q.pop(0)
                
                if node.left is not None:
                    nextQ.append([node.left, left, node.val])
                
                if node.right is not None:
                    nextQ.append([node.right, node.val, right])
                
                if left is not None:
                    ret = min(ret, node.val - left)
                
                if right is not None:
                    ret = min(ret, right - node.val)
                
            q = nextQ
            
        return ret