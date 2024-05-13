# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathMax = -math.inf
        
        
        def findMax(node):
            if node is None:
                return 0
            
            nonlocal pathMax
            
            sumLeftChild = findMax(node.left)
            sumRightChild = findMax(node.right)
            
            curMax = max(node.val, sumLeftChild + node.val, sumRightChild + node.val)
            
            
            pathMax = max(pathMax, node.val, node.val + sumLeftChild + sumRightChild, node.val + sumLeftChild, node.val + sumRightChild)
            
            return curMax
        
        findMax(root)
        
        return pathMax
            
            
        
        
        