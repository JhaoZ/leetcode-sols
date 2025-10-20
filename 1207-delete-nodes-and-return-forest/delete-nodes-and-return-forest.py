# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        ans = []


        
        def func(node):
            if not node:
                return
            
            func(node.left)
            func(node.right)
            if node.left and node.left.val in delete:
                node.left = None
            if node.right and node.right.val in delete:
                node.right = None

            if node.val in delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
        
        func(root)

        if root.val not in delete:
            ans.append(root)
        return ans
        