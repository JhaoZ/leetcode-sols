class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = set(nums)
        if min(cnt) < k:
            return -1
        else:
            if k in cnt:
                return len(cnt) - 1
            else:
                return len(cnt)
        

        