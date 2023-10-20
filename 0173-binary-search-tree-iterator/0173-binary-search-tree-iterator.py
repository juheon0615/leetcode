# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.values.append(node.val)
        self.inorder(node.right)
            
    def __init__(self, root: Optional[TreeNode]):
        self.idx = -1
        self.values = []
        self.inorder(root)

        

    def next(self) -> int:
        self.idx += 1
        return self.values[self.idx]
        

    def hasNext(self) -> bool:
        return True if self.idx + 1 < len(self.values) else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()