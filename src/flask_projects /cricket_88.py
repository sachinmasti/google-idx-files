'''menu={'roti':100,
      'dal makhani':200,
      'naan':150,
      'paneer kaju':200,
      'lacha paratha':250,
      'papad':100,
      'solkadi':150}

cart=[]
total=0

print('⭐----------MENU----------⭐')
for key, value in menu.items():
    print(f"{key:10} : {value:} INR")
print("⭐-------⭐--------⭐--------⭐----⭐")

while True:
      food = input("select your menu or a (q to quite):👉  ")
      if food=='q':
            break 
      elif menu.get(food) is not None:
       cart.append(food)
print('⭐----------YOUR ORDER----------⭐')

for food in cart:
      total += menu.get(food)
      print(food, end=' ')

print()
print(f"total is:  {total} INR")
      

import random

low=1
high=100
chance=0
number = random.randint(low,high)

while True:
      guess = int(input(f'enter your number berwen {low} to {high}'))
      chance +=1

      if guess < number:
            print(f'{guess} number is low')
      
      elif guess > number:
            print(f'{guess} number is high ')
      
      else:
            print(f"{guess } is correct")
            break

print(f"you took {chance} chances to guess the number")


lowest_number=1
higest_number=100
answer = random.randint(lowest_number,higest_number)
gueses = 0
is_running  = True
print('⭐---------GAME----------⭐')
print("Welcome to number gusing number⭐")
print(f"guess a number between {lowest_number} and {higest_number}")
while is_running:
      guess = input("enter your guess: ")
      if guess.isdigit():
            guess =int(guess)
            gueses+=1

            if guess < lowest_number or guess > higest_number:
                  print("number out of range")
                  print(f"plz enter your number between {lowest_number} to {higest_number}")

            elif guess < answer:
                  print("too low! try again")
            elif guess > answer:
                  print("to high! try again")
            else:
                  print(f"correct! the answer was {answer}")
                  print(f"you took {gueses} guesses")
                  is_running = False

      else:
            print("invalid guessed")
            print(f"enter your number between {lowest_number} to {higest_number}")'''
      

'''menu={'roti':100,
      'dal makhani':200,
      'naan':150,
      'paneer kaju':200,
      'lacha paratha':250,
      'papad':100,
      'solkadi':150}

order=[]
cost=0
name=input('enter your name:👉  ')
print(f"hi {name} welcome to our restaurent")

print('⭐----------MENU----------⭐')
for key,value in menu.items():
      print(f"{key:10} : {value} INR")
print("⭐-------⭐--------⭐--------⭐----⭐")
while True:
      your_order = input("enter your food name or a (q to quite):👉  ")
      if your_order == 'q':
            break
            print("complate your order cart💨") 
      elif menu.get(your_order) is not None:
            order.append(your_order)
print('⭐----------YOUR ORDER----------⭐')

for foods in order:
      cost += menu.get(foods)
      print(foods , end=",")

print()
print(f" your total bill is: {cost} in INR")
print('⭐----------YOUR ORDER OVER----------⭐')


def car_name(name):
      match name:
            case  'bugati':
                  print('this car is very speed')
            case 'Lamborghini ':
                  print('this car is insane')
            case 'porche':
                  print("this is very beautiful")
            case _:
                  print('this not in a list or car')

                  # comment: 


car=(car_name('porche'))
print(car)           

print('hello woild')

email=input('enter your email: ')
if '@' or '.' in email:
      print("email is valid happy journey")
else:
      print(f'your {email} is not valid enter a valid email')'''

'''car_list={'bugati':500,
           'mustang':200,
           'ferrari':400,
           'Maclaren':500,
           'bmw':300,
           'lamborghini':400,}
cars_list=[]
total_price=0
print('⭐----------MENU----------⭐')
for key,value in car_list.items():
      print(f"{key:10} {value} $")

customer =input('enter your name:  ')
print(f"welcome {customer} in our ")
print("⭐-------⭐--------⭐--------⭐----⭐")

while True:
      your_car=input('enter your car list which you buy or (q to quite):👉 ')
      if your_car =='q':
            break
      elif car_list.get(your_car) is not None:
            cars_list.append(your_car)
print('⭐----------YOUR ORDER----------⭐')
for cars in cars_list:
      total_price+=car_list.get(cars)
      print(cars,end=' ')

print()
print(f'your tatal price of your car list is {total_price}')
print('⭐----------YOUR ORDER OVER----------⭐')'''





'''list1={'sachin':400,'shramik':700,'girish':400,'shirish':800,'sudip':900,'akash':900,'prakash':900}

output=input('enter your name: ')

if output in list1:
      print(f'your name is {output} and your rank is {list1[output]}')

elif list1.get(output)  is None:
      print('this name is not in a list')



import os as o
from PIL import Image
file_path="D:\\wp13990996-grizzly-bear-4k-wallpapers.jpg"
if o.path.exists(file_path):
    print('this is a file exits😀')
    image = Image.open(file_path) 
    image.show()
else:
    print(f'no file name as {file_path}')
class Menu:

      count =0
      total_bill = 0

      def __init__(self,name,price):
            self.name = name
            self.price = price
            Menu.count +=1
            Menu.total_bill += price

      def info(self):
             print(f"{self.name} {self.price}")

      @classmethod
      def total_order(cls):
            return cls.count

      @classmethod
      def total_bills(cls):
            return cls.total_bill

order=Menu('pizaa',100)
order2=Menu('roti',200)
order3=Menu('paneer',500)

print(f'total order is {Menu.total_order()}')
print(f'total bill is {Menu.total_bills()}')


car_list={'bugati':5,
           'mustang':2,
           'ferrari':4,
           'Maclaren':5,
           'bmw':3,
           'lamborghini':4,}

cars_list=[]
print('⭐----------MENU----------⭐')

for key,value in car_list.items():
      print(f'{key:10} {value} $')

print("⭐-------⭐--------⭐--------⭐----⭐")

while True:
      your_order=input('enter your car name or a (q to quit):  ')
      if your_order == 'q':
            break

      if your_order in car_list:
            print(f'this is your order {your_order} and price tag of this guy is {car_list[your_order]} in million dollars ')
            cars_list.append(your_order)
      
      elif car_list.get(your_order) is  None:
            print(f'{your_order} is not in a our list')
      
print('⭐----------YOUR ORDER OVER----------⭐')

for cars in cars_list:
      print(cars,end=' ')

print()

import threading 
import time 

def sachin (name:str) -> None:
      time.sleep(4)  # import time  # import time
      print(f'hi my name is {name}')
      if name == 'veena':
            print(f'{name} you are a VIP❤️')

def sm () -> None:
      time.sleep(9)
      print('hi this is a end🙏')

def masti () -> None:
      time.sleep(6)
      print('hi what are you doing 👋')

if __name__ == '__main__':
      name = input('enter your name : ')
      

task1=threading.Thread(target=sachin,args=(name,))
task1.start()
task2=threading.Thread(target=sm)
task2.start()
task3=threading.Thread(target=masti)
task3.start()

task1.join()
task2.join()
task3.join()'''


men={'roti':100,
      'naan' : 150,
      'paneer' : 180,
      'dal tadaka' : 130,
      'paneer tika' : 150,
      'kaju panner' : 200,
      'papad' : 100,
      'solkadi' : 100}
your_order_list=[]
total_bill=0

print()
name=input('enter your name: ')
print('--------⭐ WELCOME ⭐--------')
print(f'Welcome {name} 🙏')
print()
print('--------⭐ MENU ⭐--------')
print()
for key,values in men.items():
      print(f" {key:10} {values} INR ")
print()
while True:
      your_list=input('enter your list of food or (s to stop order):--> ')
      if your_list.lower() == 's':
            print()
            print(f'{name} your order is complete🙃')
            break
      if your_list in men:
            print(f'your order is {your_list} and your price of order is {men[your_list]}')
            your_order_list.append(your_list)
      elif men.get(your_list) is None:
            print(f"{your_list} is not available")

print()
print('---------⭐ your order list ⭐-----------')
for lists in your_order_list:
      print(lists)
print()
print('----------⭐total bill⭐----------')
for lists in your_order_list:
      total_bill += men.get(lists)

print(f'your total bill is {total_bill}')