class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = [k for k, v in Counter(arr).items() if k == v]
        return max(a) if a else -1