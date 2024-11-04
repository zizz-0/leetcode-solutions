"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.
"""

"""
Runtime:
    0 ms
    Beats 100%
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = False
        if s:
            if s[0] == '-':
                neg = True
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
        
        num_str = ""
        for num in s:
            if num.isdigit():
                num_str += num
            else:
                break

        if not num_str:
            return 0
            
        ret_num = int(num_str)
        if neg:
            ret_num = -ret_num
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if ret_num < INT_MIN:
            return INT_MIN
        if ret_num > INT_MAX:
            return INT_MAX

        return ret_num