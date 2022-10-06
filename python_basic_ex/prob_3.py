str = input("Enter a String: ")
print(f'Orginal String is {str}')
print("Printing only even index chars")
for i in range(len(str)):
    if i%2==0:
        print(str[i])