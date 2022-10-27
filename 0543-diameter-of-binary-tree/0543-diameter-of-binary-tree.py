# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root, depth):
            nonlocal diameter
            if not root:
                return 0
            # Otherwise I want the depth of left and right subtrees
            left = dfs(root.left, 0)
            right = dfs(root.right, 0)
            max_depth = max(left, right)
            diameter = max(diameter, left + right)
            return 1 + max_depth
        dfs(root, 0)
        return diameter

        
        
        
        
        
        
        
#     ans = 0

#     def depth(p):
#         nonlocal ans
#         if not p: 
#             return 0
#         left, right = depth(p.left), depth(p.right)
#         ans = max(ans, left+right)
#         return 1 + max(left, right)

#     depth(root)
#     return ans
