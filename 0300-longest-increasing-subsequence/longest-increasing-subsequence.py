class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [[0] * (len(nums) + 1) for i in range(len(nums) + 1)]

        for i in reversed(range(len(nums))):
            for j in range(-1, i):

                if j == -1:
                    dp[i][j + 1] = max(1 + dp[i + 1][i + 1], dp[i + 1][j + 1])
                elif nums[i] > nums[j]:
                    dp[i][j + 1] = max(1 + dp[i + 1][i + 1], dp[i + 1][j + 1])
                else:
                    dp[i][j + 1] = dp[i + 1][j + 1]
        return dp[0][0]


        
        