"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        miss = 0
        
        for number in range(1, len(nums) + 1):  
                counter = nums.count(number)
                if counter == 0:
                    miss = number
                
                if counter > 1:
                    dup = number 
                
        return(dup,miss)
