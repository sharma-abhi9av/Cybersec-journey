"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # for first index is a then second is have a +n right nice
        result = []
        for i in range(0,n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
