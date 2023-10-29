# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        leaves1 = []
        leaves2 = []
        
        def getLeaves(node, leaves):
            
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            
            if node.left:
                getLeaves(node.left, leaves)
            
            if node.right:
                getLeaves(node.right, leaves)

        if root1:
            getLeaves(root1, leaves1)
        
        if root2:
            getLeaves(root2, leaves2)
        
        isSame = True
        
        if len(leaves1) != len(leaves2):
            isSame = False
        else:
            for i in range(len(leaves1)):
                if leaves1[i] != leaves2[i]:
                    isSame = False
                    
        return isSame