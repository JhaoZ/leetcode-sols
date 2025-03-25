class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:

        ans = 0
        size = count

        def check(freq):
            return all([v == count or v == 0 for k, v in freq.items()])

        while size <= len(s) and size <= 26 * count:
            freqs = {}

            # set up
            for i in range(size):
                curr = ord(s[i]) - ord('a')
                if curr not in freqs:
                    freqs[curr] = 0
                freqs[curr] += 1
            
            # first check
            if check(freqs):
                ans += 1

            
            for i in range(len(s) - size):
                curr = ord(s[i]) - ord('a')
                freqs[curr] -= 1
                if freqs[curr] == 0:
                    del freqs[curr]
                next_char = ord(s[i + size]) - ord('a')
                if next_char not in freqs:
                    freqs[next_char] = 0
                freqs[next_char] += 1
                
                if check(freqs):
                    ans += 1

            size += count
        return ans

        