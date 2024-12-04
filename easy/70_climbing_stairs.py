"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
Runtime:
    0ms
    Beats 100%
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        f, s = 1, 2
        for _ in range(3, n+1):
            f, s = s, f + s
        
        return s