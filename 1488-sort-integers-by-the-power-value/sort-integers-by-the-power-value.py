class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = [0] * (hi - lo + 1)
        idx = (hi - lo + 1) - 1

        cache = {}
        def collatz(num):
            if num == 1:
                return 0

            if num in cache:
                return cache[num]
            
            result = -1
            if num % 2 == 0:
                result = 1 + collatz(num / 2)
            else:
                result = 1 + collatz(3 * num + 1)
            
            cache[num] = result
            return cache[num]
        
        for i in reversed(range(lo, hi + 1)):
            arr[idx] = (collatz(i), i)
            idx -= 1
        
        arr.sort()        

        return arr[k - 1][1]

        