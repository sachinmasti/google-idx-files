
while True:
    s=input('enter your name: ')

    length = len(s)
    mat = length//2
    if length %2 ==0:
        print(s[mat-1:mat+1])
    else:
        print(s[mat])