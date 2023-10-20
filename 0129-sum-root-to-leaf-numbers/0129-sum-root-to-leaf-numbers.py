# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def rootToLeaf(node, cur):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return cur * 10 + node.val
            elif node.left is None and node.right is not None:
                return rootToLeaf(node.right, cur * 10 + node.val)
            elif node.left is not None and node.right is None:
                return rootToLeaf(node.left, cur * 10 + node.val)
            else:
                return rootToLeaf(node.left, cur * 10 + node.val) + rootToLeaf(node.right, cur * 10 + node.val)

        return rootToLeaf(root, 0)
        