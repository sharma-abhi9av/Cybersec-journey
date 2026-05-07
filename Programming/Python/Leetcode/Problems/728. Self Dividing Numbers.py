class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []     
        for number in range(left,right+1):
            a = True
            for digit in str(number):
                if int(digit) ==0 or number % int(digit) !=0:
                    a = False 
                    break
            if a :
                output.append(number)     
        return output
