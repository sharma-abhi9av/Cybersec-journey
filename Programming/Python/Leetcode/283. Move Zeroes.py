"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

### Thinking Process & Whiteboard
I was practicing questions related to the use of two pointers,
My initial thought was what if I replace every 0 with a non-zero number and exchange there position,
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
I got Index error,the reason behind the error is if there is no 0 in the input,the left pointer goes forward, but right pointer stays the same. 
Finally breaking the code when left pointer goes out of index. Now I knew, the base logic is correct, I just have to move right pointer everytime.
I switched to 'for' loop, using 'right' as the index of my for loop, made sure it moves everytime,the left pointer only moves when the loop finds a non-zero number,
As the loop goes forward both pointers move together until the loop hit any '0', as soon as zero comes in the way the left pointer stops,and right move ahead. 
When the loop runs again and find the nums[right] != 0, it swaps the position of left and right number respectively. Explained by a diagram below.
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

