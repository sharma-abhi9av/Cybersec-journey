class Solution:
    def isPalindrome(self, x: int) -> bool:
        mystr = f"{x}"
        return mystr == mystr[::-1]
     
