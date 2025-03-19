class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def backtrack(i):
            if i< 0:
                return True
            
            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and backtrack(i - len(word)):
                    return True
            return False
        return backtrack(len(s) - 1)
                    
        