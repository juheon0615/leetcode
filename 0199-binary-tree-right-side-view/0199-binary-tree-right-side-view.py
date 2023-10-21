# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #2:18
        
        
        ret = []
        
        #bfs
        
        if root is None:
            return root
        
        nodes = [root]
        
        while nodes:
            newNodes = []
            right = None
            
            for i in range(len(nodes)):
                if nodes[i].left is not None:
                    newNodes.append(nodes[i].left)
                if nodes[i].right is not None:
                    newNodes.append(nodes[i].right)
                
                if i == len(nodes) - 1:
                    ret.append(nodes[i].val)
            
            nodes = newNodes 
        
        return ret
                
                
        