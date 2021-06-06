# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def isSame(A,B):
            if A is None and B is None:
                return True
            if A is None or B is None:
                return False
            return A.val == B.val and isSame(A.left, B.left) and isSame(A.right, B.right)
        
        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return True
        if root is None:
            return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        
        
