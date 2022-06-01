# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def DFS(node):
            nonlocal ans
            if not node: return 0
            left_height = DFS(node.left)
            right_height = DFS(node.right)
            
            if left_height + right_height > ans:
                ans = left_height + right_height
                
            return max(left_height, right_height) + 1
        DFS(root)
        return ans
        
