print(chr(102))
print(ord('f'))
def floor(a,b):
    return a/b
print(floor(20,3))

def floor_d(a,b):
    return a//b

print(floor_d(20,3))


# l = list(map(int,input('enter your list: ').split()))
# print(f"min{min(l)},'max'{max(l)}")

# i = list(map(lambda x : x*2))
# print(i(200))

num = 5

for i in range(num , 0 ,-1):
    print('*' * i)

num = 5
for i in range(0,num+1,+1):
    print('*' * i)

num = 9
for i in range(num):
    for j in range(num):
        if i == j or j==num-1-i:
            print('*',end="")
        else:
            print(' ',end="")
    print()
print()

num = 8
col = 2*num-1
for i in range(num):
    for j in range(col):
        if i == j or j ==col - 1 -i:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    
num = 7
for i in range(num):
    print('*')
    for j in range(num):
        if i == num -1:
            print('*',end=" ")
    print()

num  = 5
for i in range(num+1):
    print('*'*i)

