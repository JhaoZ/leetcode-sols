# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = {}

        def bfs(node):
            queue = deque()
            queue.append((node, 0))

            while queue:
                curr, level = queue.popleft()
                if curr == None:
                    continue
                if level not in levels:
                    levels[level] = []
                levels[level].append(curr.val)
                
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
            
                

        bfs(root)
        print(levels)

        ans = 0
        for key, value in levels.items():
            m = {}
            for i, v in enumerate(value):
                m[v] = i
            
            for i, v in enumerate(sorted(value)):
                if value[i] != v:
                    curr = value[i]
                    ans += 1
                    value[i], value[m[v]] = value[m[v]], value[i]

                    # update map
                    temp = m[curr]
                    m[curr] = m[v]
                    m[v] = temp
           
        return ans
            
            

