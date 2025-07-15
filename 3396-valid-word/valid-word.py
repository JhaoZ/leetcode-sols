class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        t = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
        v = False
        c = False
        for i in word:
            if i.lower() not in t:
                return False
            if i.lower() in vowels:
                v = True
            if i.lower() not in vowels and i.lower() not in digits:
                
                c = True
        return v and c
        