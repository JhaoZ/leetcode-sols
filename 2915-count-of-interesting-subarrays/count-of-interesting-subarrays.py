class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        prefixes = defaultdict(int)
        curr = 0
        prefixes[0] = 1
        for n in nums:
            curr += 1 if n % modulo == k else 0
            ans += prefixes[(curr - k + modulo) % modulo]
            prefixes[curr % modulo] += 1
        return ans
            

        