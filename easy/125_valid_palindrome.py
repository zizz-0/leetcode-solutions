"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

"""
Runtime:
    7ms
    Beats 82.03%
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        print(s)
        i = 0
        for r in reversed(s):
            if r.lower() != s[i].lower():
                return False
            i += 1
        return True