# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current path sum by adding the node's value
            current_sum += node.val
            
            # Check if there is a prefix sum that we can subtract to get the targetSum
            path_count = prefix_sums[current_sum - targetSum]
            
            # Update the prefix_sums map with the current sum
            prefix_sums[current_sum] += 1
            
            # Continue the DFS on left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # After we're done with the node, backtrack: remove the current sum from the prefix_sums
            prefix_sums[current_sum] -= 1
            
            return path_count
        
        # Dictionary to store the frequency of prefix sums
        prefix_sums = defaultdict(int)
        # Initialize prefix sum 0 with count 1 to handle the case where path equals targetSum
        prefix_sums[0] = 1
        
        # Start DFS traversal from the root with an initial cumulative sum of 0
        return dfs(root, 0)

#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
#         '''
#         dfs for all nodes
#         this way, the path will aways be unique because all dfs start path will have different start node
#         '''
        
#         ret = []
#         def dfs(node, cur):
#             # print(node.val, " : ", cur)
#             cur += node.val
            
#             if cur == targetSum:
#                 ret.append(True)
            
#             if node.left:
#                 dfs(node.left, cur)
            
#             if node.right:
#                 dfs(node.right, cur)
        
        
#         def runDfs(node):
#             dfs(node, 0)
            
#             if node.left:
#                 runDfs(node.left)
#             if node.right:
#                 runDfs(node.right)
        
#         if root:
#             runDfs(root)
        
#         return len(ret)
        
        
                
        