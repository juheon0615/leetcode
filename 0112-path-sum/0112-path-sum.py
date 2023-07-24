# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
                    
        def dfs(node, target):
            if node.left is None and node.right is None and target - node.val == 0:
                return True
            
            ret = False
            if node.right is not None:
                ret = ret or dfs(node.right, target - node.val)
            
            if node.left is not None:
                ret = ret or dfs(node.left, target - node.val)
            
            return ret
        
        return dfs(root, targetSum) if root is not None else False
    
#         if root is None:
#             return False
        
#         #bfs
#         nodes = [(root, targetSum)]
#         ret = False
        
#         while nodes:
#             nextNodes = []
#             while nodes:
#                 node, target = nodes.pop(0)
                
#                 if node.right is None and node.left is None and target - node.val == 0:
#                     ret = True
#                     break
                
#                 if node.right is not None:
#                     nextNodes.append((node.right, target - node.val))
#                 if node.left is not None:
#                     nextNodes.append((node.left, target - node.val))
            
#             nodes = nextNodes
                
            
#             if ret == True:
#                 break
                
        
#         return ret
                
                
                
        