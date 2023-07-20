# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
#         q = [root]
#         level = 0
        
#         while q:
#             nextQ = []
#             cur = []
#             while q:
#                 node = q.pop(0)
#                 if node is None:
#                     cur.append(-1)
#                     continue
                
#                 nextQ.append(node.left)
#                 nextQ.append(node.right)
#                 cur.append(node.val)
            
#             print("level ",level, " cur: ", cur)
#             level += 1
#             q = nextQ        
#         return 0
        
        def dp(node, visited):
            
            if node is None:
                return 0
            
            if node in visited:
                return node.val
            
            ll = None if node.left is None else node.left.left
            lr = None if node.left is None else node.left.right
            rl = None if node.right is None else node.right.left
            rr = None if node.right is None else node.right.right
            
            
            
            maxVal = max((dp(ll, visited) + dp(lr, visited) + dp(rr, visited) + dp(rl, visited) + node.val), (dp(node.right, visited) + dp(node.left, visited)))
            
            node.val = maxVal
            visited.add(node)
            
            return node.val
        
        visited = set()
        dp(root, visited)
        
        return root.val
            
        