from practiceOne import ParenthesesChecker




pchek = ParenthesesChecker()


parentheses = "{{{"

result = pchek.is_valid(parentheses)
if result == True:
    print("Valid!")
else:
    print("Invalid!")