# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visible_tree_node(self, root: TreeNode, high: int) -> int:
        visible_cnt = 0
        if root is None:
            return 0
        if root.val >= high:
            high = root.val
            visible_cnt += 1
        l = self.visible_tree_node(root.left, high)
        r = self.visible_tree_node(root.right, high)
        return (l + r + visible_cnt)    
    def goodNodes(self, root: TreeNode) -> int:
        return self.visible_tree_node(root, -9999999999)
        
    
        