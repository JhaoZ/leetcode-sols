from collections import Counter, defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        letter_freqs = Counter(word)
        freq_letters = defaultdict(list)

        for letter, freq in letter_freqs.items():
            freq_letters[freq].append(letter)
 
        if len(freq_letters) == 1:
            return len(letter_freqs) == len(word) or len(letter_freqs) == 1

        if len(freq_letters) == 2:
            freq_1, freq_2 = freq_letters.keys()
            return (
                ((freq_1 == 1 or freq_1 - 1 == freq_2) and len(freq_letters[freq_1]) == 1) or 
                ((freq_2 == 1 or freq_2 - 1 == freq_1) and len(freq_letters[freq_2]) == 1)
            )

        return False