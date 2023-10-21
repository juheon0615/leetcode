# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ret = []
        
        def kth(node, c):
            print(node.val, " : ", c)
            curK = c
            
            if node.left is not None:
                curK = kth(node.left, curK)
            
            curK += 1
            if curK == k:
                ret.append(node.val)
            
            if node.right is not None:
                curK = kth(node.right, curK)
            
            return curK
        
        kth(root,0)
        print(ret)
        return ret[0]
        