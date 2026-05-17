"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1): # we loop through reverse.
            if digits[i] < 9:                # if digit is less then 9 just add 1 and return else make the digit 0 and loop again
                digits[i] +=1 
                return digits
            digits[i] = 0                    # if our loop reaches here that means the digit is something like [9,9,9] 
        return [1] + digits                  # so we jsut return by adding 1 in front, i.e. --> [9,9,9] --> [1,0,0,0]
