# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def BFS(root: Optional[TreeNode]):
            Queue = []
            Averages = []
            if not root:
                return None
            Queue.append(root)
            while (len(Queue) > 0):
                length = len(Queue)
                Sum = 0
                for nodes in Queue:
                    Sum += nodes.val
                avg = Sum/length
                Averages.append(avg)
                for i in range(length):
                    popped = Queue.pop(0)
                    if popped.left is not None:
                        Queue.append(popped.left)

                    # Enqueue right child
                    if popped.right is not None:
                        Queue.append(popped.right)
            return Averages
        return BFS(root)
                
                
        