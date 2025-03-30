class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        minRun = 2**31
        for num in cost:
            minRun = min(num, minRun)
            ans.append(minRun)
        return ans

        