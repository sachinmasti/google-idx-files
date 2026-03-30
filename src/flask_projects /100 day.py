# Taking input from the user and storing it in variable 'a'
'''a=input()
# Printing the value of 'a'
print(a)

# Taking name input from the user and storing it in variable 'b'
b= input("Enter your name: ")
# Printing the name entered by the user
print(b)

# Taking the first number as input and storing it in variable 'c'
c= input ("Enter your fist number:")
# Taking the second number as input and storing it in variable 'd'
d=input("Enter your second number:")
# Printing the concatenation of 'c' and 'd' (treating them as strings)
print(c+d)
# Converting 'c' and 'd' to integers and printing their sum
print(int(c)+int(d))

# Assigning the value 5 to variable 'h'
h= 5
# Assigning the value 98 to variable 'k'
k= 98

#print(h+k)
#print(h-k)
#print(h*k)
#print(h/k)
#print(h%k)
#print(h//k)
#print(h**k)'''
#accessing the characters in a string

#name="veena"
#print("Hey,"+name)
#print(name[0])
#print(name[1])
#print(name[2])
#print(name[3])
#print(name[4])

# looping in string
#data= 'data "science" is  a very good'
'''print(data)
for charcter in data:
    print(charcter)
#accessing the characters in a string

friends= "vrushali"
print(friends[0])
print(friends[1])
print(friends[2]) 
print(friends[3]) 
print(friends[4])
print(friends[5])
print(friends[6])
print(friends[7])
print(friends[8])'''

'''#string length 
names ="veena,pallavi,shivani"
print(names[0:5])
print(len(names))'''

'''flower= "rose,jasmine,lily,azalea"
print (flower[0:4]) 
print(len(flower))
print(flower[0:3])
print(flower[4:8])'''
 
'''nm="veena"
print(nm[-4:-2])

fruit ="mango"
print(fruit[0:4])
print(fruit[:])
print(fruit[-3:-2])
print(fruit[-5:-1])'''
#string
'''v="veena"
print(v.upper())  
print(v.lower())
print(v.capitalize())
p="!!!pallavi!!!!!"
print( p.rstrip("!"))
a="welcome to bca" 
print (a.center(50))
print(a.count("o"))
print(a.endswith("v"))
print(a.find("to"))
print(v.replace("vrushali","veena"))
print(a.title())
print(a.split())
print(a.swapcase())
print(a.startswith("w"))
print(a.index("to"))'''
#if else statement

'''age=int(input("Enter your age: "))
if (age>=18):
    print("you engible for vote")
else:
    print("you are not engible for vote")   

drive=int(input("Enter your age:"))
if(drive>=18):
    print("you are engible for drive")
else:
    print("you are not engible for drive")

num=int(input("Enter your number= "))
if(num%2==0):
    print("your number is even")
else:
    print("Your number is odd")

#if elif else statement
num=int(input ("Enter your number: "))
if(num>0):
    print("Your number is postive")
elif(num<0):
    print("your number is negative")
else:
    print("your number is zero")'''

'''x=int(input("Enter your number: "))

if (x==5):
    print("x is 5")
elif (x < 5):
    print("x is less than 5")
else:
    print("x is grater than 5")'''

#nested if else statement
'''p=int(input("Enter your number= "))
if(p%2==0):
    print("your number is even")
    if(p%4==0):
        print("your number is divisible by 4")
    else:
        
            print("your number is not divisible by 4")
            if(p%6==0):
                print("your number is divisible by 6")
            else:
                print("your number is not divisible by 6")
else:
    print("your number is odd")'''

import time
timestamp=time.time()
time.strftime('%h:%m:%s')
print(timestamp)
timestamp(strftime('%h'))
print(timestamp)
timestamp(strftime('%m'))
print(timestamp)
timestamp(strftime('%s'))
print(timestamp)

    
    
    




