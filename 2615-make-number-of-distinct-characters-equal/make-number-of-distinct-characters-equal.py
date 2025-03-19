class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        for key1, val1 in freq1.items():
            for key2, val2 in freq2.items():
                
                size1 = len(freq1.keys())
                size2 = len(freq2.keys())

                if key2 not in freq1:
                    size1 += 1
                if val1 == 1 and (not (key2 == key1)):
                    size1 -= 1
                
                if key1 not in freq2:
                    size2 += 1
                if val2 == 1 and (not (key2 == key1)):
                    size2 -= 1
                
                if size1 == size2:
                    return True
        return False

        