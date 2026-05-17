"""
Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.


"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        number_list = list(range(1, n+1))
        for i in range(len(number_list)):
            if sum(number_list[:i+1])== sum(number_list[i:]):
                return number_list[i]
        return(-1)
