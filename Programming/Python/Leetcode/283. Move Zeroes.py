"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

### Thinking Process & Whiteboard
Here is how I visualized the two-pointer approach:
So, i knew i have to use two pointers as i was practising questions with tag as two pointers
My initial thought was what if i replace every 0 with a number and exchange there position,
then I started visualing, and finally made a thought. 
```
left = 0
right = 1        
while right < len(nums):
    if nums[left] != 0:
        left += 1
    elif nums[right] == 0:
        right += 1 
    else: 
        nums[right] != 0
        nums[left] = nums[right]
        nums[right] = 0
        left += 1
        right += 1 
    return nums
``` 
As expected i got index error, the reason behind the error is if there is no 0 in the input,
the left pointer goes forward, but right pointer stays the same, finally breaking the code when left pointer goes out of index.
Now i knew, the logic is correct, i just have to move right pointer everytime, so I switched to 'for' loop.
The for loop moves right pointer everytime as I used right as index, the left pointer only moves when the loop finds a non-zero number,
the pointers move together until they hit any '0', as soon as zero comes in the way the left pointer stops,and right move ahead, when the loop runs again and find the nums[right] != 0, it swaps the position of left and right number respectively.
![283. Move Zeroes](pictures/283_move_zeroes.png)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

