# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        queue = [root]
        
        level = 0
        maxLevel = 0
        maxSum = -math.inf
        while queue:
            level += 1
            nextQueue = []
            
            levelSum = 0
            for node in queue:
                levelSum += node.val
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            
            queue = nextQueue
        
        return maxLevel
