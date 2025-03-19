class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            ans += word1[p1]
            p1 += 1
            ans += word2[p2]
            p2 += 1
        
        if p1 == len(word1) and p2 == len(word2):
            return ans
        elif p1 < len(word1):
            ans += word1[p1:]
            return ans
        else:
            ans += word2[p2:]
            return ans