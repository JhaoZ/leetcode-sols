class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right_side = defaultdict(int)

        dom = -1

        for i in nums:
            right_side[i] += 1
            if dom == -1 or right_side[i] > right_side[dom]:
                dom = i
        
        dom_cnt = right_side[dom]
        
        split = -1
        for i in range(len(nums)):
            right_side[nums[i]] -= 1

            if right_side[dom] > ((len(nums) - i - 1) // 2) and (dom_cnt - right_side[dom]) > ((i + 1) // 2):
                return i 
        return split
        