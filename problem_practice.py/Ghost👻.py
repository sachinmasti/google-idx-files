
from colorama import Fore, Style,init
init(autoreset=True)
#print a X shape
row = 7
for i in range(row):
    for j in range(row):
        if i == j or j == row -1 - i:
            print(f"{Fore.CYAN}*", end=' ')
        else:
            print(" ",end=" ")
    print()


import create_pattern as cp

# cp.word('veena','*')
# cp.word('sachin','*')

print()


print('--------------------------------')


# print a v shape 
row = 7
col = 2 * row -1
for i in range(row):
    for j in range(col):
        if i == j or j == col -1 -i:
            print(f"{Fore.LIGHTMAGENTA_EX}*" ,end=' ')
        else:
            print('',end=' ')
    print()
    
#print a inverted v
row = 7
col =2*row-1
for i in range(row):
    for j in range(col):
        if j == row - 1 -i or j ==row -1 +i:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

print('-⭐'*10)


#print a L shape
row = 7
for i in range(row):
    print('*')
    for j in range(row):
        if i ==row-1 :
            print('*',end=" ")
        
    print()
print(f'{Fore.CYAN}sachin masti')

#print a L shape
row = 7 
for i in range(row):
    if i == row -1:
        print('*' * row)
    else:
        print('*')

name =  'python'
if name == 'java' or name== 'rust':
    print('truee')
else:
    print('falsee')



import math as m
print(m.sqrt(10))
print(m.lcm(3,40))
num_1 = int(input('enter your num: '))
num_2 = int(input('enter your second num: '))
print(m.lcm(num_1,num_2))
print(f'{Fore.CYAN}{m.sqrt(num_1)}')


add = lambda x,y:x+y
a=12
b=30
print(add(a,b))