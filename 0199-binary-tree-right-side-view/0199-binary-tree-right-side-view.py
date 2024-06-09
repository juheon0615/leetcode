# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        queue = [root]
        ret = []
        while queue:
            nextLevel = []
            ret.append(queue[-1].val)
            for node in queue:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            queue = nextLevel
        return ret

        