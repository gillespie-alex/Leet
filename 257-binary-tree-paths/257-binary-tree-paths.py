# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        str_path = ""
        paths = []
        if root.right is None and root.left is None:
            return str_path + str(root.val)
        return self.DFS(root, str_path, paths)
    def DFS(self, root, str_path, paths):
        #first check if the inputted tree even exists 
        if not root:
            return
        
        str_path = self.helper_function(str_path, root)

        #in this case we now want to append the string to the List as this is the end of the root to leaf path
        if root.right is None and root.left is None:
            paths.append(str_path)
            return
        self.DFS(root.left, str_path, paths)
        self.DFS(root.right, str_path, paths)
        return paths
       

    def helper_function(self, string, root):
        #first case where we only want to add the root and no arrow
        if not string:
            string = string + str(root.val)
            return string
        #helper function used for intermediate non-leaf nodes that need to be added to the string path
        string = string + '->' + str(root.val)
        return string

