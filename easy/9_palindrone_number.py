"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

"""
Runtime:
    3ms
    Beats 88.05%
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]