"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []     
        for number in range(left,right+1):
            status = True
            for digit in str(number):
                if int(digit) ==0 or number % int(digit) !=0:
                    status = False 
                    break
            if status :
                output.append(number)     
        return output
