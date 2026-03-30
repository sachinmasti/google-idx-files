name = ['sachin','shirish','girish','pramod','rohit','virat']
new = list(map(str.capitalize, name))
new1 = tuple(map(str.upper,name))
print(new)
print(new1)

number = [1,3,4,5,6,3,5,7,3,9]
new_num = list(map(lambda x : x**2,number))
print(number)
print(set(number))
print(set(new_num))

from  colorama import Fore , Style
print( Fore.LIGHTRED_EX+'this is a filter prictce' + Style.RESET_ALL)
# filter fucntion practice 
news = list(filter(lambda x: True if x >2 else False,number))
print(news)
print(Fore.YELLOW+ 'hare krisha⭐' + Style.RESET_ALL)

new2 = list(filter(lambda x : x%2==0 , number))
print(new2)

s = [1,23,2,1,3,344,3,26,5,7,675,4,4,8,10]
s= new2
print(s)

print(Fore.LIGHTYELLOW_EX + 'Hare Krisha 🌻')
print(Fore.MAGENTA + 'sachin masti❤️‍🔥' + Style.RESET_ALL)


a =15
b=3
def count_no(a,b):
    b =str(b)
    count = 0
    for k in range(a+1):
        s =str(k**2)
        count += s.count(b)
    return count

sm = count_no(a,b)
print(sm)

str_ = 'sachin masti'
print(str_.swapcase())

def cube(fx,value):
    return 5 + fx(value)

ms = lambda x : x* x * x
print(cube(ms,2))

list_num = [1,2,3,4,1,2,3,4,5,6]
count = 0
for num in list_num:
    count^=num
print(count)

age = 20
if age >= 18 or age <18:
    print('you are eligible for vote')
else:
    print('you are not eligible for vote')

x = 11
y=x^1
print(y)

list = [1, 2, 3, 2, 1]
result = 0
for num in list:
    result ^= num
print(result)  # Output: 3 (unique number)
print(Fore.CYAN + 'Sachin masti that is a my name❤️‍🔥' + Style.RESET_ALL  )
print('sachin'.center(30))
name = 'Sachin masti that is a my name⭐'
print(Fore.LIGHTMAGENTA_EX + name.center(80) + Style.RESET_ALL )


lst = [1,2,3,4,5,6,6,7,5,4,3,3,4,5,6]
lst1=list(filter(lambda x: x!=5,lst))
print(lst1)

lst = [1,2,3,4,5,6,7,8,8,9]
result = list(map(lambda x:x*x*x,lst))
print(result)

new = list(filter(lambda x : True if x>5 else False,lst))
print(new)

from functools import reduce
new3 = reduce(lambda x,y:x+y,lst)
print(new3)


lst = [1,2,3,4,5,6,7,8,8,9]
lst2 = [34,5,3,5,6,7,7,5,3,2,567,8,6,4,3,2]
lst3 = [12,3,4212,3,46,4,67,8,7,3,2,77,6,5]
new_line1 = map(lambda x:x**2,filter(lambda x,y,z:x>5,lst,lst2,lst3))
print(list(new_line1))
