# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return 
        def DFS(root: Optional[TreeNode]):
            view = []
            Queue = []
            Queue.append(root)
            while Queue:
                for i in range(len(Queue)):
                    popped = Queue.pop(0)
                    if i == 0:
                        view.append(popped.val)
                        
                    if popped.right and popped.left:
                        Queue.append(popped.right)
                        Queue.append(popped.left)
                        
                    elif popped.right:
                        Queue.append(popped.right)
                    
                    elif popped.left:
                        Queue.append(popped.left)
            return view
        return DFS(root)
        