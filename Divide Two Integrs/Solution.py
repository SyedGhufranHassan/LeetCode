class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
    MIN = -2**31

    
    if dividend == MIN and divisor == -1:
        return MAX

    
    if (dividend < 0) ^ (divisor < 0):
        s = -1 
    else:
        s=1

    
    dividend, divisor = abs(dividend), abs(divisor)

    
    q= 0
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        dividend -= temp_divisor
        q += multiple

    
    if s > 0:
        q=q
    else:
        q=-q

    
    return min(max(MIN, q), MAX)
