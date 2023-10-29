# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        '''
        dfs for all nodes
        this way, the path will aways be unique because all dfs start path will have different start node
        '''
        
        ret = []
        def dfs(node, cur):
            # print(node.val, " : ", cur)
            cur += node.val
            
            if cur == targetSum:
                ret.append(True)
            
            if node.left:
                dfs(node.left, cur)
            
            if node.right:
                dfs(node.right, cur)
        
        
        def runDfs(node):
            dfs(node, 0)
            
            if node.left:
                runDfs(node.left)
            if node.right:
                runDfs(node.right)
        
        if root:
            runDfs(root)
        
        return len(ret)
        
        
                
        