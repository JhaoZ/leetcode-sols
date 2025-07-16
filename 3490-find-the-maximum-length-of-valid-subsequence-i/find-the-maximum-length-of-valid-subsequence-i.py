class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        
        #all even
        evens = len([num for num in nums if num % 2 == 0])
        # all odds
        odds = len([num for num in nums if num % 2 != 0])
        
        #odd even
        odd = True
        oddeven = 0
        for n in nums:
            if odd and n % 2 == 1:
                oddeven += 1
                odd = False
            elif not odd and n % 2 == 0:
                oddeven += 1
                odd = True
        evenodd = 0
        odd = False
        for n in nums:
            if odd and n % 2 == 1:
                evenodd += 1
                odd = False
            elif not odd and n % 2 == 0:
                evenodd += 1
                odd = True
        
        return max(evens, odds, oddeven, evenodd)
        