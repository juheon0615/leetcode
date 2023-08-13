# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = [root]

        level = 1        
        max_sum = -pow(10,5) - 1
        
        ret = 0
        while q:
            nextQ = []
            level_sum = 0
            while q:
                node = q.pop(0)
                level_sum += node.val
                
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            
            if level_sum > max_sum:
                ret = level
                max_sum = level_sum
            
            q = nextQ
            level += 1
        
        return ret
