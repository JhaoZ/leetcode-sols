# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def func(curr):
            if not curr:
                return 0

            l1 = func(curr.left)
            l2 = func(curr.right)
            levels[max(l1, l2)].append(curr.val)
            return max(l1, l2) + 1
            
        ans = []
        func(root)
        for i in range(len(levels)):
            ans.append(levels[i])
        return ans