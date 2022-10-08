""" Write a program to check if one string contains another. For example, the result will be True if all the characters in the s1 are present in s2, otherwise False. The character’s position doesn’t matter. Take inputs from the user.

s1 = "Phi"
s2 = "Phitron"

Output : True
 """
s1 = "Phi"
s2 = "Phitron"

s1_count = 0

for char in s1:
    found = 0;
    for c in s2:
        if char == c:
            found += 1
            break
    if found: s1_count += 1

if s1_count == len(s1):
    print(True)
else:
    print(False)

