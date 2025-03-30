class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def palindrome(s1):
            return s1 == s1[::-1]
        
        ans = 1
        if palindrome(s):
            ans = max(ans, len(s))
        if palindrome(t):
            ans = max(ans, len(t))
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                for a in range(len(t)):
                    for b in range(a, len(t) + 1):
                        first = s[i:j]
                        second = t[a:b]
                        if palindrome(first + second):
                            ans = max(ans, len(first + second))
        return ans

        