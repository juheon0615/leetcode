# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def getNodeLength(node):
            nonlocal ret

            if node is None:
                return 0
            else:
                leftMax = getNodeLength(node.left)
                rightMax = getNodeLength(node.right)
                ret = max(ret, leftMax + rightMax)
                return max(leftMax, rightMax) + 1
        
        getNodeLength(root)
        return ret
        