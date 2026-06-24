/*
Given an integer x, return true if x is a , and false otherwise.

Example 1:
```
Input: x = 121
Output: true
```
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
```
Input: x = -121
Output: false
```
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

*/
#include <limits.h>
bool isPalindrome(int x) {
    int num;
    int y=0;
    int p = x;
    if (p < 0) {
        return false;
    }
    while (p != 0) {
        num = p % 10;
        p = p / 10  ;
        if (y > INT_MAX/10){
            return false;
        }
        y = (y*10) + num;
    }
    if (x == y){
        return true;
    }
    return false;
}
