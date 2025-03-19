# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        best = None
        def traverse(node):
            if not node:
                return False
            nonlocal best
            left = traverse(node.left)
            right = traverse(node.right)
            if left and right:
                best = node
                return True
            if node == p and (left or right):
                best = node
                return True
            if node == q and (left or right):
                best = node
                return True
            
            return node == p or node == q or left or right
        traverse(root)
        return best
            


