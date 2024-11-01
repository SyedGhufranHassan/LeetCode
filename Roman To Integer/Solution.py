class Solution:
    def romanToInt(self, s: str) -> int:
        roman= {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
        sum = 0
        previous = 0
        
        for symbol in reversed(s):
            value = roman[symbol]
            
            
            if value < previous:
                sum -= value
            else:
                sum += value
                
            previous = value

        return sum
            
