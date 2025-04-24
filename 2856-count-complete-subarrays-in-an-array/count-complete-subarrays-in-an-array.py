class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_cnt = len(set(nums))
        ans = 0
        k = 0
        freq = defaultdict(int)
        end = 0
        for start in range(len(nums)):

            while end < len(nums) and k < distinct_cnt:
                freq[nums[end]] += 1
                if freq[nums[end]] == 1:
                    k += 1
                end += 1
            
            if k == distinct_cnt:
                ans += len(nums) - (end - 1)
            
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                k -= 1
        return ans


        