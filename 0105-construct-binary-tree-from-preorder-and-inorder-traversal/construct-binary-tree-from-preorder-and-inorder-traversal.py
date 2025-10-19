# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = preorder[0]
        inorder_left = []
        left_set = set()
        inorder_right = []
        right_set = set()
        left = True
        for n in inorder:
            if n == root:
                left = False
                continue
            if left:
                inorder_left.append(n)
                left_set.add(n)
            else:
                inorder_right.append(n)
                right_set.add(n)
        
        preorder_left = [n for n in preorder if n in left_set]
        preorder_right = [n for n in preorder if n in right_set]

        curr = TreeNode(val = root)
        curr.left = self.buildTree(preorder_left, inorder_left)
        curr.right = self.buildTree(preorder_right, inorder_right)
        return curr
        
