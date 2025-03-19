# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        def recur(node, temp):
            if node.left == None and node.right == None:
                if temp:
                    temp += '->' + str(node.val)
                else:
                    temp +=str(node.val)
                ans.append(temp)
                return
            
            if temp:
                temp += '->' + str(node.val)
            else:
                temp += str(node.val)
            if node.left:
                recur(node.left, temp)
            if node.right:
                recur(node.right, temp)
        recur(root, "")
        return ans
            
        