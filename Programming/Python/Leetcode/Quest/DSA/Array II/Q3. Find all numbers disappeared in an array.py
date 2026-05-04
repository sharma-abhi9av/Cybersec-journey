class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        result = []
        for number in range(1, len(nums)+1):
            if number not in set_nums:
                result.append(number)
        return result
