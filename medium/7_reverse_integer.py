"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

"""
Runtime:
    25ms
    Beats 97.63%
"""
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        rev = ""

        if(x < 0):
            x_str = x_str.strip("-")
            
        for num in x_str[::-1]:
            rev += num

        reversed_int = int(rev)

        if(x < 0):
            reversed_int = -reversed_int

        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int