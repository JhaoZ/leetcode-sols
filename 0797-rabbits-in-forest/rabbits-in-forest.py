class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        freq = Counter(answers)
        for key, val in freq.items():
            occur = val // (key + 1) + (0 if val % (key + 1) == 0 else 1)
            ans += occur * (key + 1)
        return ans
        