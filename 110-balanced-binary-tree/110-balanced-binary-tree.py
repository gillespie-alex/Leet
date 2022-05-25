# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0,True
        l,bool1 = self.DFS(root.left)
        r,bool2 = self.DFS(root.right)
        bool_check = True
        if abs(l - r) > 1:
            bool_check = False
        bool_test = (bool1 and bool2)
        return max(l,r) + 1, (bool_check and bool_test)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x,check = self.DFS(root)
        return check
    
        