from typing import List

class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        def min_unsorted_length(window: List[int]) -> int:
            n = len(window)
            
            # Step 1: Find the first index where order breaks (left to right)
            start = 0
            while start < n - 1 and window[start] <= window[start + 1]:
                start += 1

            if start == n - 1:
                return 0  # Already sorted

            # Step 2: Find the last index where order breaks (right to left)
            end = n - 1
            while end > 0 and window[end - 1] <= window[end]:
                end -= 1

            # Step 3: Find min and max in the unsorted region
            min_unsorted = min(window[start:end+1])
            max_unsorted = max(window[start:end+1])

            # Step 4: Expand boundaries
            while start > 0 and window[start - 1] > min_unsorted:
                start -= 1
            while end < n - 1 and window[end + 1] < max_unsorted:
                end += 1

            return end - start + 1

        ans = []
        for start in range(len(nums) - k + 1):
            window = nums[start:start + k]
            ans.append(min_unsorted_length(window))
        return ans
