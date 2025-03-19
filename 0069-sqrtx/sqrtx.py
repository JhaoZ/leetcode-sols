class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low < high:
            mid = low + (high - low + 1) // 2
            if mid * mid <= x:
                low = mid
            else:
                high = mid - 1
        return low
        