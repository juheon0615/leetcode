# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def inOrder(node, ret):
            if node is None:
                return
            inOrder(node.left, ret)
            ret.append(node.val)
            inOrder(node.right, ret)
        
        inOrder(root, ret)
        return ret
            
        