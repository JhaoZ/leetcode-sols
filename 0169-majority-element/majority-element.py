class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = Counter(nums)
        for key, val in f.items():
            if val >= len(nums) / 2:
                return key