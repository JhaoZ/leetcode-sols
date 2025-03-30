class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        ans = []
        curr_size = 0
        seen = set()

        for i in range(len(s)):
            seen.add(s[i])
            freq[s[i]] -= 1
            curr_size += 1
            if freq[s[i]] == 0:
                seen.remove(s[i])
            if len(seen) == 0:
                ans.append(curr_size)
                curr_size = 0
        return ans
            
        