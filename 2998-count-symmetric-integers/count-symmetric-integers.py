class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            curr = str(i)
            if len(curr) % 2 == 0:
                if sum([int(ch) for ch in curr[:len(curr)//2]]) == sum([int(ch) for ch in curr[len(curr)//2:]]):
                    ans += 1
        return ans

        