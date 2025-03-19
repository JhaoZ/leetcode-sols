class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = nums[i]

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if left > i + 1 and nums[left - 1] == nums[left]:
                    left += 1
                elif nums[left] + nums[right] + target == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif nums[left] + nums[right] < (-target):
                    left += 1
                else:
                    right -= 1
        return ans
        