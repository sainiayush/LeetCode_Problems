# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def calculate_diameter(node):
            if not node:return 0
            left = calculate_diameter(node.left)
            right = calculate_diameter(node.right)
            self.diameter = max(self.diameter, left+right)
            
            return 1 + max(left,right)
    
        self.diameter = 0
        calculate_diameter(root)
        return self.diameter
            
            
            
            
