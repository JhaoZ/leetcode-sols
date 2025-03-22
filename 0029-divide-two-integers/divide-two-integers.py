class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        # Once the divisor is bigger than the current dividend,
        # we can't fit any more copies of the divisor into it anymore */
        while divisor >= dividend:
            # We know it'll fit at least once as divivend >= divisor.
            # Note: We use a negative powerOfTwo as it's possible we might have
            # the case divide(INT_MIN, -1). */
            powerOfTwo = -1
            value = divisor
            # Check if double the current value is too big. If not, continue doubling.
            # If it is too big, stop doubling and continue with the next step */
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            # We have been able to subtract divisor another powerOfTwo times.
            quotient += powerOfTwo
            # Remove value so far so that we can continue the process with remainder.
            dividend -= value

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient