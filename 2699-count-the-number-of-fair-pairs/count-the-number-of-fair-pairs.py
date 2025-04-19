class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        arr = SortedList()
        ans = 0

        for i in range(len(nums)):
            if not arr:
                arr.add(nums[i])
            else:
                left_side = arr.bisect_left(lower - nums[i])
                right_side = arr.bisect_right(upper - nums[i])
                ans += right_side - left_side
                arr.add(nums[i])
        return ans
        