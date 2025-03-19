class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for _, val in freq.items():
            if val % 2 != 0:
                return False
        return True
        