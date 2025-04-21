class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maxnum = 0
        minnum = 0

        curr = 0
        for d in differences:
            curr += d
            minnum = min(minnum, curr)
            maxnum = max(maxnum, curr)
        
        return max((upper - maxnum) - (lower - minnum) + 1, 0)


        