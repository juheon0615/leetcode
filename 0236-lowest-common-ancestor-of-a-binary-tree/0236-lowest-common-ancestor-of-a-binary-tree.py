# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ret = []
        
        def search(node):
            if node is None: 
                return 0
            
            found = 0
            if node.val == p.val or node.val == q.val:
                found += 1        
            
            found += search(node.left) + search(node.right)
            if found == 2:
                ret.append(node)
            
            return found
        
        search(root)
        return ret[0]
