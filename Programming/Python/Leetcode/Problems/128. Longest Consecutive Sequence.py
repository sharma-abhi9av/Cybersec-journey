"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rep = []
        counter = 1
        nums = set(nums) 
        if not nums:
            return 0
        for num in nums:
            if (num - 1) not in nums: 
                while num + 1 in nums: 
                    counter += 1
                    num += 1       
            rep.append(counter)
            counter = 1  
        return max(rep)
        
