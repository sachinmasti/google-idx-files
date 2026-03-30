from colorama import Fore,Style,init
init(autoreset=True)

def my_func(n) -> None:
    for i in range(n):
        print(f"{Fore.CYAN} {'*' * (i+1)}")

my_func(5)

def sunflower(n) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

sunflower(5)

def bmw(n) -> None:
    for i in range(n,0,-1):
        print(f"{Fore.RED} {'*' * i}")
bmw(5)

def trangle(rows) -> None:
    rows = 4
    for i in range(1, rows + 1):
        # Print spaces to align the pyramid
        print(" " * (rows - i), end="")
        # Print stars with spaces between them
        print("* " * i)

trangle(4)


def diamond (n):
    mid = n //2
    # pehala pattern 
    for i in range(1,mid+1):
        print('_' * (mid - i),end='')
        print('* ' * i)
    # dusara pattern 
    for i in range(mid-1,0,-1):
        print(' ' * (mid - i),end='')
        print('* ' * i)

diamond(10)