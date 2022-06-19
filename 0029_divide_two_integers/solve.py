class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Exclude the only case when overflow might happen
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_positive = True
        if dividend < 0:
            is_positive = not is_positive
            dividend = -dividend
        if divisor < 0:
            is_positive = not is_positive
            divisor = -divisor

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            q = 1
            d = divisor

            # speed up calculation by doubling the divisor each round
            while dividend >= d:
                dividend -= d
                q += q
                d += d

            quotient += q

        if is_positive:
            return quotient
        return -quotient
