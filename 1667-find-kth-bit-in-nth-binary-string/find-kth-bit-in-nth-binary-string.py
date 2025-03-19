class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        length = 1 << n
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        elif k == length // 2:
            return '1'
        else:
            bit = self.findKthBit(n - 1, length - k)
            return '1' if bit == '0' else '0'