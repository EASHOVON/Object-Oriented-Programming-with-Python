food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter your tip percentage %: '))

def calculateFoodTotal(food: float,tip_percentage: float) -> float:
    tip = food * (tip_percentage/100)
    total = food+tip
    print('--------------------------------')
    print(f'🥘 Food Amount: ${food}')
    print(f'⚖️ Tip Amount: ${tip}')
    print('\n')
    print(f'💰 Total Amount: ${total}')
    print('--------------------------------')
    return total

calculateFoodTotal(food_amount,tip_percentage)