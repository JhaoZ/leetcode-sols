class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_sum(s):
            ans = 0
            while s > 0:
                ans += s % 10
                s //= 10
            return ans

        freq = defaultdict(int)
        max_v = 0
        for i in range(1, n + 1):
            curr = digit_sum(i)
            freq[curr] += 1
            max_v = max(max_v, freq[curr])
        
        ans = 0
        for k, v in freq.items():
            if v == max_v:
                ans += 1

        return ans

        