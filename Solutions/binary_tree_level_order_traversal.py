# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        level = [root]
        
        while level and root:
            
            currentNode = []
            nextLevel = []
            
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            output.append(currentNode)
            level = nextLevel
        return output
