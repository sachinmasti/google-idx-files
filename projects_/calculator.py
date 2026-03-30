from colorama import Fore, Style, init
init(autoreset=True) # Initialize colorama to automatically reset colors after each print statement

import math as m # Import the math module (though it's not used in the current code)

# Get the user's name for a personalized welcome message
your_name = input('enter your name👉🏼:')
print(f"{Fore.LIGHTMAGENTA_EX} ⭐-----Welcome to calculator {your_name}-----⭐")
print() # Print an empty line for better formatting


while True: # Start an infinite loop for the calculator operations
    oprators = ['+', '-', '*', '/', '//', '%'] # Define a list of valid operators

    # Get the first number from the user
    num1 = input(f"{Fore.LIGHTYELLOW_EX}enter your first number or q to stop➡️: ")
    if num1.lower() == 'q': # Check if the user wants to quit
        print(f'{Fore.LIGHTRED_EX}your opration is stoped🙃')
        break # Exit the loop if the user enters 'q'
    try:
        num1 = int(num1) # Convert the input to an integer
    except ValueError: # Handle cases where the input is not a valid number
        print('enter a valid number')
        continue # Continue to the next iteration of the loop

    # Get the second number from the user
    num2 = input(f"{Fore.LIGHTBLUE_EX} enter your second number➡️: ")
    try:
        num2 = int(num2) # Convert the input to an integer
    except ValueError: # Handle cases where the input is not a valid number
        print(f'{Fore.RED} enter a valid number')
        continue # Continue to the next iteration of the loop

    # Get the desired operation from the user
    prompt = input(f'{Fore.GREEN}enter your prompt or q to stop +,-,*,/,//,%👉🏼:  ')
    
    # Check if the entered prompt is a valid operator
    if prompt not in oprators:
        print(f'{Fore.RED}enter a valid oprator')
        continue # Continue to the next iteration if the operator is invalid
    
    # Perform the chosen operation based on the 'prompt'
    if prompt == '+':
        print(f"{Fore.LIGHTCYAN_EX} {num1 + num2}") # Addition
    elif prompt == '-':
        print(f'{Fore.LIGHTCYAN_EX}{num1 - num2}') # Subtraction
    elif prompt == '*':
        print(f"{Fore.LIGHTCYAN_EX}{num1 * num2}") # Multiplication
    elif prompt == '/':
        if num2 == 0: # Handle division by zero
            print(f'{Fore.RED}Cannot divide by zero!')
        else:
            print(f'{Fore.LIGHTCYAN_EX}{num1 / num2}') # Division
    elif prompt == '%':
        if num2 == 0: # Handle modulus with zero
            print(f"{Fore.RED}Cannot take modulus with zero!")
        else:
            print(f'{Fore.LIGHTCYAN_EX}{num1 % num2}') # Modulus
    elif prompt == '//':
        if num2 == 0: # Handle floor division by zero
            print(f"{Fore.RED}Cannot floor divide by zero!")
        else:
            print(f'{Fore.LIGHTCYAN_EX}{num1 // num2}') # Floor division
    else:
        # This 'else' block should technically not be reached due to the 'if prompt not in oprators' check above,
        # but it serves as a fallback for any unhandled cases.
        print(f'{Fore.LIGHTRED_EX}Invalid operation. Try again.')

# Messages displayed after the loop breaks (when the user quits)
print(f"{Fore.LIGHTBLUE_EX}✔️ All operations completed successfully.")
print(f"{Fore.CYAN}Thank you, {your_name}, for using this calculator. Goodbye! 👋")

