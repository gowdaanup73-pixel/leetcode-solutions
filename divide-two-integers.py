class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == 0:
            return 0
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0
        for i in range(31, -1, -1):          
            if (b << i) <= a:                 
                a -= (b << i)
                quotient += (1 << i)          
        quotient = -quotient if negative else quotient
        return max(INT_MIN, min(INT_MAX, quotient))
