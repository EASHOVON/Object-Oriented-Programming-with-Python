# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order. 

# For example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class ParenthesesChecker:
    def is_valid(self, parenthesis):
        stack = []
        for char in parenthesis:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        return not stack

