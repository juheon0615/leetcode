"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs approach
        # extra space will be the number of nodes in each row
        
        if root is None:
            return root
        
        level = [root]
        
        while level:
            nextLevel = []
            
            for i in range(len(level)):
                if level[i].left is not None:
                    nextLevel.append(level[i].left)
                if level[i].right is not None:
                    nextLevel.append(level[i].right)
                
                if i == len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i+1]
            
            level = nextLevel
        
                
        
        return root