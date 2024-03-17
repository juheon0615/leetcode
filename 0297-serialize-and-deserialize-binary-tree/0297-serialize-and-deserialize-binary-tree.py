# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''
            0
            1 2 
            3 4 5 6
        7 8 9 10 11 12 13 14
        
        left -> self * 2 + 1
        right -> *2 + 2 
        '''
        if root is None:
            return "None"
        retNodes = []
        
        def dfs(node, index):
            
            retNodes.append("%d:%d" % (node.val, index))
            
            if node.left is not None:
                dfs(node.left, index * 2 + 1)
            if node.right is not None:
                dfs(node.right, index*2 + 2)
            
        dfs(root, 0)        
        return " ".join(retNodes)
            
            
            
        
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        
        splits = data.split(" ")
        
        nodes = {}
        for split in splits:
            val, index = split.split(":")
            val = int(val)
            index = int(index)
            
            node = TreeNode(val)
            nodes[index] = node
        
        
        q = [0]
        while q:
            nextLevel = []
            
            for nodeIndex in q:
                left = nodeIndex * 2 + 1
                right = nodeIndex * 2 + 2
                
                if left in nodes:
                    nodes[nodeIndex].left = nodes[left]
                    nextLevel.append(left)
                if right in nodes:
                    nodes[nodeIndex].right = nodes[right]
                    nextLevel.append(right)
            
            q = nextLevel
            
        return nodes[0]
        
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))