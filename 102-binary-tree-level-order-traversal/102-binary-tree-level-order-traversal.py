# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(root: Optional[TreeNode]):
            if not root:
                return None
            Queue = []
            output = []
            Queue.append(root)
            while (len(Queue) > 0):
                temp = []
                for i in range(len(Queue)):
                    node = Queue.pop(0)
                    temp.append(node.val)
                    if node.left is not None:
                        Queue.append(node.left)
                    if node.right is not None:
                        Queue.append(node.right)
                output.append(temp)
            return output
        return BFS(root)
        