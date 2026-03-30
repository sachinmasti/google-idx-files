'''s='sachin'
for i in range(1,3):
    print(i)


while True:
    number=int(input('enter your numbaer: '))
    if number == 45:
        print('this is a your lucky numaber😀')
        break
    elif number >= 100:
        print('this number is not allowed 🐩')
    elif number <= 10:
        print('this number is very small😀')
    
    else:
        print('this is not a match your number🙃')


name = ['sachin','shirish','shramik','sudip','girish']
while True:
    your_name=input('enter your name: ' )

    if your_name in name:
            print('this name is already exits')
    elif your_name == 'stop':
            print('your list is ended ')
            break
    else:
            print('this name is not exits')

import random
my_number=random.randint(1,100)
while True:
    number=int(input('enter your number: '))
    if number >= 100:
        print('this number is not valid🙃')
        break
    elif number == my_number:
        print('you are a guessed right number 😀')
    
    elif number <=1:
        print('this is not valid 🫎')
    else:
        print('carry on🌻')



import random

my_number = random.randint(1, 100)

while True:
    number = int(input('Enter your number: '))

    if number < 1 or number > 100:
        print('This number is not valid 🙃 Please enter a number between 1 and 100.')
        continue

    if number == my_number:
        print('You guessed the right number! 😀')
        break  # Stop the loop when guessed correctly
    elif number < my_number:
        print('Too low! Try again 🌻')
    else:
        print('Too high! Try again 🌻')


import random
sachin=random.randint(1,100)
print(sachin)

def repeat_string(n, s):
    return s * n
print(repeat_string(3, "Hi"))     # Output: "HiHiHi"
print(repeat_string(0, "Hello"))  # Output: ""
print(repeat_string(5, "A"))      # Output: "AAAAA"

import random
pc_number = random.randint(1,100)
while True:
    user_number = int(input('enter your guessing number: '))
    if user_number < 1 or user_number > 100:
        print('your number is not valid please enter a number between 1 and 100')
        continue
    if user_number == pc_number:
        print('you are a  guessed right number ⭐🫎')
        break
    elif user_number < pc_number:
        print('your number is low plz enter a right number ')
    else:
        print('nuber is to big')

def game(p1,p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or \
         (p1 == 'scissors' and p2 == 'paper') or \
         (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'player 2 won⭐'

print(game('rock', 'scissors')) 
print(game('scissors', 'rock'))  
print(game('paper', 'paper'))    

def no_space():
    name=input('enter your name: ')
    return name.replace(" ","")

names=no_space()
print(names)

def grow(arr):
    first_num = 1
    for result in arr:
        first_number *= result
    return first_number

import math
def grow(arr):
    return math.prod(arr)
result= grow([1,2,3,4])
print(result)

def DNA_strand(dna):
    # code here
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return " ".join(complement [x] for x in dna )

car_liis=['bugati','bmw','proche','ferrari']
new_list=[]
for c in car_liis:
    new_list.append(c[0])
print(new_list)



def sequance(**name):
    return list(name[::2])
s=['ssachin', 'shirish', 'girish', 'guru', 'pramod', 'rohit', 'virat']
n=[sequance(name) for name in s]
print(n)

def factorial(num):
    if num==1 or num==0:
        return 1

    else:
        return num*factorial(num-1)
num=int(input('enter your number: '))
fact=factorial(num)
print(fact)

name='sachin'
print(name.center(50))

def fibonachhi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonachhi(num-1) + fibonachhi(num-2)
num=int(input('enter your number: '))
fib=fibonachhi(num)
print(fib)

def short_lst(data):
    return ['senior' if age >=55 and handicape >7 else 'open' for age,handicape in data]

data=[[34,64],[55,34],[23,60],[53,23]]
sm=short_lst(data)
print(sm)

def my_lst(points):
    rasult=[]
    for age,handicape in points:
        if age >=55 and handicape>7:
            rasult.append('senior')

        else:
            rasult.append('open')
    return rasult
points=[[24,41],[45,63],[26,52],[53,43]]
rasult=my_lst(points)
print(rasult)   

my_dict={1:'Sachin',
        2:'veen',
        3:'pramod',
        4:'putti',
        5:'sakshi',
        6:'shramik'}
for key,vales in my_dict.items():
    print(key,vales)

print(my_dict[2])
print(my_dict.pop(1))

for i in range(10):
    print(i)
    # if i==5:
    #     break
else:
    print('loop is successfully working ')


# This function calculates speed based on a given value (n).
def speed(n):
    import math
    # Calculates the speed by dividing 100000 by 3600 and then using math.floor to get the integer part.
    return (math.floor(n*(100000/3600)))

# Calls the speed function with the value 20.88 and assigns the result to vsm.
vsm=speed(20.88)
# Prints the value of vsm, which represents the calculated speed.
print(vsm)


# Define a function called 'sm' that takes an integer 'n' as input.
def sm(n):
    count = 0  # Initialize a counter to keep track of the number of iterations.
    while n > 9:  # Continue the loop as long as 'n' is greater than 9.
        p = 1  # Initialize a variable 'p' to 1 in each iteration.
        for d in str(n):  # Convert 'n' to a string and iterate over its digits.
            p *= int(d)  # Multiply 'p' by the integer value of each digit.
            n = p  # Update 'n' with the product 'p'.
        count += 1  # Increment the counter after each iteration.
    return count  # Return the final count.

# Get user input for a number and convert it to an integer.
n=int(input('enter your number: '))
# Call the 'sm' function with the user's number and store the result in 'ms'.
ms=sm(n)
# Print the result stored in 'ms'.
print(ms)


# Define a function named 'ms' that takes an integer 'num1' as input.
def ms(num1):
    count = 0  # Initialize a counter to 0.
    while num1 > 9:  # Continue the loop as long as 'num1' is greater than 9.
        vi = 1  # Initialize a variable 'vi' to 1 in each iteration.
        for ro in str(num1):  # Convert 'num1' to a string and iterate over its digits.
            vi *= int(ro)  # Multiply 'vi' by the integer value of each digit.
            num1 = vi  # Update 'num1' with the product 'vi'.
        count += 1  # Increment the counter after each iteration.
    return count  # Return the final count.
# Get user input for a number and convert it to an integer.
num1=int(input('enter your number: '))
# Call the 'ms' function with the user's number and store the result in 'ra'.
ra=ms(num1)
# Print the result stored in 'ra'.
print(ra)'''

name_list=['virat','rohit','sachin','shirish','girish']

for i,k,in enumerate(name_list):
    print(i+1,k)
    print(str(i)[: :-1],k[::-1])

print()











# Function to break down a number into its place value components.
def divid(num):
    # Convert the number to a string to iterate over its digits.
    num_str = str(num)
    # Calculate the length of the number string.
    length = len(num_str)
    # Initialize an empty list to store the parts.
    parts = []
    # Iterate over the digits of the number string with their index.
    for i, d in enumerate(num_str):
        # Check if the digit is not zero.
        if d != '0':
            # Append the digit with the appropriate number of trailing zeros to parts.
            parts.append(d + '0' * (length - i - 1))
    # Join the parts with ' + ' and return the resulting string.
    return ' + '.join(parts)
# Call the divid function with 45045 and print the result.
# num= int(input('enter your number: '))
di=divid(87655)
print(di)

# Define a function called 'rep' that takes a list as input.
def rep(lst):
    # Initialize a counter to keep track of the number of characters that appear more than once.
    count= 0
    # Initialize an empty list to store the characters that appear more than once.
    new_list= []
    # Iterate through each unique character in the lowercase version of the input list.
    for c in set(lst.lower()):
        # Check if the count of the current character in the lowercase version of the list is greater than 1.
        if lst.lower().count(c) > 1:
            # If the character appears more than once, increment the counter.
            count+=1
            # Add the character to the new_list.
            new_list.append(c)
    # Return the count and the new_list.
    return count,new_list

sml=rep('asdffsaddsffadsf')
print(sml)

from collections import Counter

def co(lst):
    lst = lst.lower()
    text=Counter(lst)
    duplicate = sum(1 for char in text.values() if char > 1)
    return duplicate

sm=co('asdffsaddsffadsf')
print(sm)


def sachin1(num):
    count=0
    length= []
    for i in set(num.lower()):
        if num.lower().count(i) > 1:
            count+=1
            length.append(i)

    return count , length

ms=sachin1('asdffsaddsffadsf')
print(ms)



name=['bugati','ferrari','bmw','porche','mustang']
new_c=sum(word.count('a')for word in name)
print(new_c)

def count_w(world, letter):
    return world.count(letter)
c=count_w('hello','l')
print(c)


# age=int(input('enter your age: '))
age=22

ali='passed' if age >= 18 else 'fail'
print(f'Your age is {age}, and you have {ali}.')
print(ali)


def massti(s):
    s = s.lower()
    for i in 'abcdefghijklmnopqrstuvwxyz':
         if i not in s:
            print(f"Missing: {i}")
            return False
    return True

print(massti('the quick brown fox jumps over the lazy dog'))

def isogram(s):
    return len(s) == len(set(s.lower()))

print(isogram('the quick brown fox jumps over the lazy dog'))

print(isogram(' sachin'))

sm= 'the quick brown fox jumps over the lazy dog'
print(sm.split())


def souce(array):
    odd = sorted((x for x in array if x%2!=0),reverse=True)
    return [x if x%2==0 else odd.pop() for x in array]

my_list=[1,4,42,5,33,24,6,234,456,3,2,1]
print(souce(my_list))

def msati(a,b):
    return [result for result in range(a,b+1)]
          
a=1
b=10
print(msati(a,b))

def alternative(s):
    return ''.join(
        char.upper()if char.islower() else char.lower()
        for char in s
    )
    return s.swapcase()
s='hi my Name Is SAchin MaStI'
print(s)
print(alternative(s))



dict1 = {
    1 : 'bugati',
    2 : 'bmw',
    3 : 'ferrar',
    4 : 'mercedes',
    5 : 'mustnag'}
for key in dict1.keys():
    print(dict1[key])

try:
    num = [1,2,3,4,5]
    you_num = int(input('enter your number: '))
    print(num[you_num -1])
except ValueError:
    print(f'{you_num}  is a invalid number ')
except IndexError:
    print('invalid index')

import pandas as pd
print(dir(pd))

import this

n