"""
Given a string s, find the length of the longest substring without repeating characters.
"""

"""
Runtime:
    35ms
    Beats 20.49%
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substr = []

        for char in s:
            if char in substr:
                while char in substr:
                    substr.pop(0)
            substr.append(char)
            longest = max(longest, len(substr))
        
        return longest