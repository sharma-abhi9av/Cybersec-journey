"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
```
Input: n = 3
Output: ["1","2","Fizz"]
```
Example 2:
```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [str(i) for i in range(1,n+1)]
        output[2::3] = ["Fizz"] * (n//3)
        output[4::5] = ["Buzz"] * (n//5)
        output[14::15] = ["FizzBuzz"] * (n//15)
        return(output)
