class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        list_of_count =[]
        for i, number in enumerate(nums): 
            count = 0
            for j in nums:
                if number > j:
                    count += 1 
            list_of_count.append(count)

        return list_of_count
