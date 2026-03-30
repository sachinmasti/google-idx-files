while True:
    try:
        a =int(input('enter your number 1: '))
        b=int(input('enter your second number2: '))
        print(f'sum all number is {a+b}')
    except Exception as e:
        print('enter a valid number',e)
        
