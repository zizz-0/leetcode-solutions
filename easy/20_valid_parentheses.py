"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
"""

"""
Runtime:
    0ms
    Beats 100%
"""
class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '(': ')',
            '[': ']', 
            '{': '}'
        }

        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            elif len(stack) == 0 or i != chars[stack.pop()]:
                return False
        return len(stack) == 0