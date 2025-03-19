class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        levels = defaultdict(list)

        for i in range(len(nums)):

            for j in range(len(nums[i])):
                levels[j + i].append(nums[i][j])
        
        ans = []
        for i in range(len(levels.keys())):

            ans += levels[i][::-1]
        return ans