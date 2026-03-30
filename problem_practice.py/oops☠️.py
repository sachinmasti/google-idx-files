# class person:
#         car_no = 0
#         def __init__(self,name,type,price):
#             self.name = name
#             self.type = type
#             self.price = price
#             self.__class__.car_no +=1
        
#         def info(self):
#             from colorama import Fore ,Style,init
#             init(autoreset=True)
#             print(f'car name is {Fore.CYAN}{self.name} \n car type is {Fore.GREEN}{self.type} \n car price is {Fore.RED}{self.price}')

# s = person('bugati','hyper_car','2.5M$')
# s.info()
# print(person.car_no)
# sm = person('mercedes','super car','1.2M$')
# sm.info()
# print(person.car_no)


from colorama  import Style,Fore,init
from abc import ABC,abstractmethod
init(autoreset=True)


class sports:
    count = 0
    @abstractmethod
    def __init__(self,name,type,origin):
        self.name = name
        self.type = type
        self.origin = origin
        sports.count += 1
        
    def speck(self):
        print('bark🐩')
    
    def hello(self):
        print('hello friends😈')

    
class Cricket(sports):
    def info(self):
        print(f'the name of sports is {self.name}\n the type of sports is {self.type}\n the origin of sports is {self.origin}')
        super().speck()

class Football(sports):
    
    def info(self):
        print(f'the name of sports is {self.name}\n the type of sports is {self.type}\n the origin of sports is {self.origin}')
        super().hello()


class Tennis (sports):
    def info(self):
        print(f'the name of sports is {self.name}\n the type of sports is {self.type}\n the origin of sports is {self.origin}')
        

sm = Cricket('cricket','ground','England')
sm.info()
print(sports.count)
print()

sm1=Football('Football','ground','England')
sm1.info()
print(sports.count)

sm2 = Tennis('Tennis','ground','England')
sm2.info()
print(sports.count)



# for i in (Football(),Cricket(),Tennis()):
#     i.info()
#     print()

row = 7
for i in range(row):
    for j in range(row):
        if i == j or j ==row-1-i:
            print(f'{Fore.RED}'+'*',end="")
        else:
            print(' ',end=" ")
    print()


class Employees:
    # company = 'google'
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age  # Added age to the __init__ method
    @classmethod
    def company(cls):
        print(cls.company)

    @property
    def first_name(self):
        n = self.name.split(' ')
        return n[0] , n[1]

    @first_name.setter
    def first_name(self, first): # Changed method name and parameter name
        l = self.name.split(' ')
        new_name = f'{first} {l[1]}'
        self.name = new_name

vs = Employees('pramod masti', 23, 45000)
print(vs.first_name) # Accessing the property directly
vs.first_name = 'sachin' # Using the setter
print(vs.name)
# print(Employees.company())


class Candidate:
    candidate = 0
    def __init__(self,name,age,post):
        self.name = name
        self.age = age
        self.post = post
        self.__class__.candidate +=1

    @property
    def post_info(self):
        x=self.post.split(' ')
        return x[0]

    @staticmethod
    def sum_all_num(a,b):
        return a+b

    @post_info.setter
    def change_post(self,new_post):
        y = self.post.split(" ")
        new_post = f' {y[1]}'
        self.post = new_post

    def show(self):
        print(f'the name of candidate is {self.name}\n the age of candidate is {self.age}\n the post of candidate is {self.post}')
    
sachin = Candidate('veena',19,'junior devloper')
sachin.post_info
sachin.show()
# print(sachin.post_info)
print(f'{Fore.RED}{Candidate.candidate} is a candidate number')
sachin.change_post = 'manager'
# print(sachin.post)

sachin1=Candidate('pramod',19,'whitehat hacker')
# sachin.show()
sachin1.change_post='manager'
sachin1.show()
print(f'{Fore.RED}{Candidate.candidate} is a candidate number')
print(sachin1.sum_all_num(10,20))

    

# while True:
#     print(eval(input('enter you num: ')))

