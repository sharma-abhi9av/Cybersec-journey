"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(":")","[":"]","{":"}"}
        stack = []
        for bracket in s: 
            if bracket in hashmap:
                stack.append(bracket)
            if bracket in ')}]': 
                if not stack or hashmap[stack.pop()] != bracket:
                    return False
        return len(stack) == 0 
