"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
```
Input: nums = [1,1,1], k = 2
Output: 2
```
Example 2:
```
Input: nums = [1,2,3], k = 3
Output: 2
```
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashtable = {0:1}
        current_sum = 0 
        counter = 0 
        for num in nums:
            current_sum += num
            target = current_sum - k 
            if target in hashtable:
                counter += hashtable[target]
            if current_sum not in hashtable:
                hashtable[current_sum] = 1 
            else:
                hashtable[current_sum] +=1
        return counter
