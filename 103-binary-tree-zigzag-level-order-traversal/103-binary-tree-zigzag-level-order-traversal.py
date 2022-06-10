# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(root: Optional[TreeNode]):
            if not root: return None
            queue = []
            res = []
            queue.append(root)
            counter = 0
            while len(queue) > 0:
                counter += 1
                temp = []
                for i in range(len(queue)):
                    node = queue.pop(0)
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if counter % 2 == 0:
                    #reverse the temp array every other level in the tree
                    temp = temp[::-1]
                res.append(temp)
            return res
        return BFS(root)