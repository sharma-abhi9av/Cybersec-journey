"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # make for loop
        current = 0
        maximum = 0 
        for i, num in enumerate(nums):
            if num == 1:
                current += 1 
                
            if maximum < current:
                maximum = current
            if num ==0:
                current = 0     
        
        return maximum 
