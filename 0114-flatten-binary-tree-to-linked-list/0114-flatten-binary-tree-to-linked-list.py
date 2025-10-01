# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root

        stack = []
        if cur:
            stack.append(cur)
        ordered = []
        while stack:
            node = stack.pop()
            ordered.append(node)
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)

        cur = root
        if cur:
            cur.left = None
        for i in range(1, len(ordered)):
            cur.right = ordered[i]
            cur.left = None
            cur = cur.right
            
        




