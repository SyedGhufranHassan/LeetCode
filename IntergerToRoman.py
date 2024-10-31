#Problem question Link:
#https://leetcode.com/problems/integer-to-roman/description/

#Solution Answer Link
#https://leetcode.com/problems/roman-to-integer/submissions/1439167610/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman= {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
        sum = 0
        previous = 0
        
        for s in reversed(s):
            value = roman[s]
            
            
            if value < previous:
                sum -= value
            else:
                sum += value
                
            previous = value

        return sum
