class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:

        ans = 0

        for k in range(1, 27):
            # for all possible unique character counts
            # we are trying to find substrings with k unique characters of freq == count
            freqs = [0] * 26
            unique_cnt = 0
            for i in range(len(s)):
                length = k * count  # length of the substrings we are considering
                curr = ord(s[i]) - ord('a')
                freqs[curr] += 1
                if freqs[curr] == count:
                    unique_cnt += 1
                
                # move the window
                if i >= length:
                    char_curr = ord(s[i - length]) - ord('a')
                    if freqs[char_curr] == count:
                        unique_cnt -= 1
                    freqs[char_curr] -= 1
                
                # if the unique amt of characters inside a certain window = k
                # we add 1 to answer
                if unique_cnt == k:
                    ans += 1
        return ans
                
        
        