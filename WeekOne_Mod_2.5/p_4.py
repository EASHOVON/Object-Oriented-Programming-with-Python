while True:  
    number = input()
    if number!="Quit":
        intNum = int (number)
        if intNum<0:
            print(f'{intNum} is Negetive')
        elif intNum==0:
            print(f'{intNum} is Non Negetive')
        else:
            print(f'{intNum} is Positive')
    else:
        break