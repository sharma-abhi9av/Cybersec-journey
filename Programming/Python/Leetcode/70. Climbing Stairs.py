"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

# Thinking Process and Diagram 
![70. Climbing Stairs](pictures/70_climbing_stairs.png)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # pattern, gap of last two is the next gap 
        if n in [1,2,3]:
            return n 
        dich = {
            1:1,
            2:2,
            3:3,
        }
        for i in range(4,n+1):
            dich[i] = dich[i-1]+dich[i-2]
        return dich[n]
