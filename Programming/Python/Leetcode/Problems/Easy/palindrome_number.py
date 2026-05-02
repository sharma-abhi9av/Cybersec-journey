class Solution:
    def isPalindrome(self, x: int) -> bool:
        numlist = list(str(x))
        numlist2 = []

        for i in range(len(numlist) - 1, -1, -1):
            numlist2.append(numlist[i])

        if numlist2 == numlist:
            return True
        else:
            return False               
