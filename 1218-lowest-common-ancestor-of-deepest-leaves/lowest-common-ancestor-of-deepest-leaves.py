# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ans = None

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)

            return max(left, right) + 1

        
        def recurse(node):
            nonlocal ans
            if not node:
                return
            left = depth(node.left)
            right = depth(node.right)

            if left == right:
                ans = node
            elif left < right:
                recurse(node.right)
            else:
                recurse(node.left)
        recurse(root)
        return ans