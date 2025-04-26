class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        def solve(subarr):
            minCnt = 0
            maxCnt = 0

            ans = 0
            end = 0
            for start in range(len(subarr)):
                while end < len(subarr) and (minCnt == 0 or maxCnt == 0):
                    if subarr[end] == minK:
                        minCnt += 1
                    if subarr[end] == maxK:
                        maxCnt += 1
                    
                    end += 1
            
                if minCnt !=0 and maxCnt != 0:
                    ans += len(subarr) - (end - 1)
                
                if subarr[start] == minK:
                    minCnt -= 1
                if subarr[start] == maxK:
                    maxCnt -= 1
            return ans
        
        partitioned = []
        temp = []
        for n in nums:
            if minK <= n <= maxK:
                temp.append(n)
            else:
                partitioned.append(temp.copy())
                temp = []
        if temp:
            partitioned.append(temp)
        
        ans = 0
        for p in partitioned:
            ans += solve(p)
        return ans
        