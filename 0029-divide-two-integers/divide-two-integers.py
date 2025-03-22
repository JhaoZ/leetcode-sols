class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        int_max = 2**31-1
        int_min = -2**31
        half = int_min//2

        if dividend == int_min and divisor == -1:
            return int_max

        neg_result = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False


        dividend = -abs(dividend)
        divisor = -abs(divisor)

        quotient = 0

        while divisor >= dividend:

            powers = -1
            curr_divisor = divisor
            while curr_divisor >= half and curr_divisor * 2 >= dividend:
                print(curr_divisor)
                powers *= 2
                curr_divisor *= 2
            
            quotient += powers
            dividend -= curr_divisor
        
        return quotient if neg_result else -quotient
        



        