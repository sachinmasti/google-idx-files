def a():
    print("a")

def b():
    print("b")

def c():
    print('c')

def default ():
    print(option ,'not found')

option   = input("enter your option")

func = {'a':a,'b':b,'c':c}
func.get(option,default)()


name='sachin','veena'
no=8

new_name=dict.fromkeys(name, no)
print(new_name)


while True:
    a = input('enter your car name: ')
    match a:
        case 'bugati':
            print('this is a bugati')

        case 'bmw':
            print('this is a bmw')
        
        case 'mustang':
            print('this is a mustang')
        
        case 's':
            print( 'this is a end')
            break 
        
        case _:
            print(a, 'this is not a valid car')

while True:
    name=input('enter yuor name: ')
    match name:
        case 'sachin':
            print(f'your name is {name} ')
        case 'girish':
            print(f'your name is {name}')
            print(len(name))
        case 'shirish':
            print(f'your name is {name}')
        case _:
            print('your are out of this list')
            break
        