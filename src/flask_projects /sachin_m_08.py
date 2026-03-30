# coloum=int(input("enyer your col no :👉 "))
# rows=int(input("enter your rows :👉 "))
# your=input("enter your input :👉 ")
# for i in range(coloum):
#     for y in range(rows):
#         print(your,end=" ")
#     print() 

# y_input=input("enter your choise 👉: ")
# while True:
#  match y_input:
#     case 'cricket':
#         print("this is insane❤️❤️❤️")
#         break
#     case 'football':
#         print("this is good🥵🥵")
#     case _:
#         print("invalid input ")
#         break

a=[9,8,7,6,5,4,3,2,1]
# a.sort(reverse=False)
# print(sorted(a))
for i in sorted(a):
    print(i)
# print(a)

my_list=[("sachin",100),
         ("shirish",500),
         ('girish',600),
         ('aksh',400)]
# my_list.sort(key=lambda my_list:my_list[1])
# print(my_list)
def jls_extract_def():
    for i in sorted(my_list):
        print(i)
    return i


i = jls_extract_def()
# print(my_list))
a=20
b=30
ab=lambda x,y:x+y
print(ab(a,b))

s=90
m=800
print(ab(s,m))

cars=['bugati',
      'Ferrari',
      'Lamborghini',
      'Porche',
      'McLaren']
for i,things in enumerate(cars):
    print(i+1,things)
lenth={car:len(car) for car in cars}
print(lenth)

w=[1,2,3,5,4,23,4,12,3,2]
most=max(w)
print(most)
print(max(w))
'''import time
import random
import pyautogui as png

while True:
    x=random.randint(600,400)
    y=random.randint(600,400)
    png.moveTo(x,y,0.5)
    time.sleep(5)'''

my_list=['sachin','virat','rohit','dhoni','yuvraj','grirish']
for i,things in enumerate(my_list):
    print(i+1,things)
    lenth={car:len(car) for car in my_list}
print(lenth)

'''while True:
    your_name=input('enter your name : ')
    if my_list in your_name:
            print("your are a legend👽")
    else:
            print("you are not valid🙃")
            break     my_list = ["John", "Doe"]
'''
while True:
    your_name = str(input('enter your name : '))
    if your_name in my_list:
        print("your are a legend👽")
    else:
        print("you are not valid🙃")
        break
s = lambda x, y: x + y
print(s(10,20))


s={'a':200,'b':300,'c':4050}
m={'c':400,'d':500}
sm=s|m
print(sm)


