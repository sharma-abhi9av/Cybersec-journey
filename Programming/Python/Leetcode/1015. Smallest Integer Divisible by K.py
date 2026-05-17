"""
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:    
        n = 1 % k 
        for i in range(1,k+1):
            if n == 0: 
                return i 
            n = (n*10 + 1 ) % k 
        return -1
