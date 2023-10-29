# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ret = 0
        '''
        recursive approach
        pass to next recursion if it is from left or right
        if passing the recursion to a oppsite(left->right or right-> left) increment count
        else. reset the count
        
        update on recursive. call. -> can be optimized
        
        '''
        
        def path(node, fromLeft, cnt, p):
            nonlocal ret
            
            if cnt > ret:
                ret = cnt
        
            if node.left:
                if fromLeft:
                    p = []
                    p.append("node.val")
                    path(node.left, True, 1, p)
                else:
                    p = p[:]
                    p.append(node.val)
                    path(node.left, True, cnt + 1, p)
            
            if node.right:
                if fromLeft:
                    p = p[:]
                    p.append(node.val)
                    path(node.right, False, cnt + 1, p)
                else:
                    p = []
                    p.append(node.val)
                    path(node.right, False, 1, p)
        
        if root.left:
            path(root, True, 0, [])
        
        if root.right:
            path(root, False, 0, [])
        
        return ret
            
            
            
            
            
        
        
        