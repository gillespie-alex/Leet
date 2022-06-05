"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def BFS(root: Optional[TreeNode]):
            Queue = []
            if not root:
                return None
            Queue.append(root)
            while (len(Queue) > 0):
                length = len(Queue)
                for i in range(length):
                    popped = Queue.pop(0)
                   
                    if popped.left is not None:
                        Queue.append(popped.left)

                    # Enqueue right child
                    if popped.right is not None:
                        Queue.append(popped.right)
                        
                    #if we are at the end of the level the next pointer should point to NULL
                    if i == length - 1:
                        popped.next = None
                    else:
                        popped.next = Queue[0] 
            return root
        return BFS(root)
        