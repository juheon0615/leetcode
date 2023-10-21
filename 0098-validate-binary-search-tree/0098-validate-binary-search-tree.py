# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = []
        
        def validate(node, valMin, valMax):
            if node is None:
                return
            
            if valMin is not None:
                if node.val >= valMin:
                    ret.append(node)
                    return 
            if valMax is not None:
                if node.val <= valMax:
                    ret.append(node)
                    return
                
            validate(node.left, node.val, valMax)
            validate(node.right, valMin, node.val)
        
        validate(root, None, None)
        
        return len(ret) == 0