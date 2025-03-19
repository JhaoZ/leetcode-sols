class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                graph[accounts[i][j]].append(i)
        
        visited = set()
        ans = []

        def dfs(current_account, temp):
            visited.add(current_account)

            for i in range(1, len(accounts[current_account])):
                temp.add(accounts[current_account][i])
                for j in graph[accounts[current_account][i]]:
                    if j not in visited:
                        dfs(j, temp)
        
        for i in range(len(accounts)):
            if i not in visited:
                temp = set()
                dfs(i, temp)
                temp = list(temp)
                temp.sort()
                temp.insert(0, accounts[i][0])
                ans.append(temp)
        return ans
