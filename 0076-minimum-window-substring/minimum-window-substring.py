class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = 10**9
        left = -1
        right = -1
        target_freq = Counter(t)

        freq = defaultdict(int)
        counter = 0
        start = 0
        for end in range(len(s)):
            freq[s[end]] += 1

            if freq[s[end]] == target_freq[s[end]]:
                counter += 1
            
            while counter >= len(target_freq):
                if end - start + 1 < ans:
                    left = start
                    right = end
                    ans = end - start + 1
                
                if freq[s[start]] == target_freq[s[start]]:
                    counter -= 1
                freq[s[start]] -= 1
                start += 1
        return s[left:right+1]
        