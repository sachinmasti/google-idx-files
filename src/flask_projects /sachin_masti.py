'''balance =2000
while True:
    try:
        your_output=float(input("enter your amount : "))
        if your_output<5000:
            print("insufficient balance")   
        else:
            print("your balnce is good")
        break
    except ValueError:
        print("invalid input")
balance+=your_output
print(balance)


# your_name=input("enter your name : ")
# while True:
#  if your_name in['sachin','girish','aksh','shirish']:
#     print("you are pass")
#     break
    
#  else:
#     print("you are fail")
    

while True:
    your_name = input("enter your name : ")
    students_list= ['sachin', 'girish', 'aksh', 'shirish']
    if your_name in students_list:
        print("you are pass")
        break
    else:
        print("you are fail")'''

'''list1=[1,2,3,4,5,56,7,7,88,9,900,]
first, second,*other=list1
print(first)
print(other)

abc=['a','b','c','d','e','a','c','d']
from collections import OrderedDict
unique_abc=list(OrderedDict.fromkeys(abc))
print(unique_abc)
abcd=set(abc)
print(abcd)'''

'''my_lis=[1,3,2,5,4,8,6,7,5,0,9,8]
from collections import OrderedDict
list_my=list(OrderedDict.fromkeys(my_lis))
print(list_my)
print(type(list_my))
print(set(my_lis))
if 1 and 4 in my_lis:
    print("this is insane👽👽")'''


'''names=['sachin','girish','shirish','shramik','sudip']
while True:
    try:
       your_input=str(input('enter yur sudent name : '))
       if your_input in names:
         print("you are pass")
       elif your_input.isdigit():
            print('this is invalid input')
        
       else:
        print("you are fail")
    except SyntaxError:
        print("you are give a wrong input🙃")
        break
    finally:
        print("this is your result ")
'''

'''my_list=['sachin','shirish','girish','akash','babu','virat']
my_list.sort()
print(my_list)
if 'sachin' or 'virat' in my_list:
    print("you are a legend ")
number=[0,9,8,7,6,5,4,3,2,1]
number.sort()
print(number)

balnce=2000
while True:
    try:
        your_amount=float(input("enter your amount :👉 "))
        if your_amount<5000:
            print("your balnce is insuficient")
        elif your_amount>10000:
                print("your amount is insane")
        else:
            print("your balnce is good")
            break
    except ValueError:
        print("invalid input 👌")
    finally:
        print("this is your result")
balnce+=your_amount
print(balnce)'''


'''my_list=[]
while True:
    your_list=input('enter your game :👉 ')
    if 'cricket' in your_list:
        print("this is a fentastic game🦁")
        break
    else :
        print('carry on your list ')
        lenth={game:len(game) for game in my_list}
        print(lenth)
        my_list.append(your_list)

print('this is your games🔥',my_list)'''

'''my_list = []
while True:
    your_list = input('Enter your game:👉 ')
    if 'cricket' in your_list:
        print("This is a fantastic game🦁")
        break
    else:
        print('Carry on your list')
        my_list.append(your_list)
        lenth = {game: len(game) for game in my_list}
        print(lenth)

print('This is your games🔥', my_list)'''

from functools import partial

def cars(car_name:str,car_price:int,car_type:str) ->None:
    print(f'this car name is {car_name} \n car price is {car_price}\n and car type is {car_type}💕')

new_var=partial(cars,car_type='combustion engine 🦁')
new_var('bugati',20000)
new_var('lambo',1220000)
new_var('bmw',120000)

from functools import cache

from random import choice,sample

my_list=['achin','girish','akash','Rohit','virat']
new_list=choice(my_list)
new_list=sample(my_list,k=2)
print(new_list)


sm=[1,2,3,4,12,134,5,6,7,8,9,10]
print(sm.sort())


